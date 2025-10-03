from swarm import Agent, Result
from swarm.repl import run_demo_loop
from routines import *
from tools import *

INTENT_TO_POLICY_MAP = {
    'update_address': {
        'POLICY': UPDATE_ADDRESS_POLICY,
        'FUNCTIONS': [change_address]
    },
    'transaction_status': {
        'POLICY': TRANSACTION_STATUS_POLICY,
        'FUNCTIONS': [get_transaction_history, get_all_acct_details]
    },
    'account_balance': {
        'POLICY': ACCOUNT_BALANCE_POLICY,
        'FUNCTIONS': [get_all_acct_balances]  
    }
}

def transfer_to_orchestrator():
    """Transfer control back to the Orchestrator Agent"""
    return Result(
        value="Let me transfer you back to our main menu.",
        agent=orchestrator_agent,
        context_variables={}
    )

def escalate_to_agent():
    """Escalate to a human agent"""
    return Result(
        value="Let me transfer you to a live agent who can help you better.",
        agent=None,
        context_variables={}
    )

def get_agent_policy(policy_type: str):
    """Get the appropriate policy and functions based on policy type"""

    if policy_type not in INTENT_TO_POLICY_MAP:
        raise ValueError(f"Unknown policy type: {policy_type}")

    policy_content = INTENT_TO_POLICY_MAP[policy_type]['POLICY']
    functions = INTENT_TO_POLICY_MAP[policy_type]['FUNCTIONS']

    return STARTER_PROMPT + policy_content, functions + [transfer_to_orchestrator, escalate_to_agent]

def transfer_to_fulfillment(policy_type: str):
    """Generic transfer function that can handle any policy type"""
    # Get the appropriate policy and functions
    policy, functions = get_agent_policy(policy_type)
    
    # Update fulfillment agent with new policy and functions
    fulfillment_agent.instructions = policy
    fulfillment_agent.functions = functions
    
    return Result(
        value=f"I'll help you with that.",
        agent=fulfillment_agent,
        context_variables={"policy_type": policy_type}
    )

# Initialize the orchestrator agent
orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions=ORCHESTRATOR_INSTRUCTIONS,
    temperature=0.7,
    functions=[transfer_to_fulfillment,
        escalate_to_agent
    ]
)

# Initialize the fulfillment agent with default policy
default_policy, default_functions = get_agent_policy("transaction_status")
fulfillment_agent = Agent(
    name="Fulfillment Agent",
    instructions=default_policy,
    functions=default_functions
)

if __name__ == "__main__":
    print("Welcome to Financial Services! How can I help you?")
    run_demo_loop(orchestrator_agent, context_variables={})

