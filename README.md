# Multi-Agent IVR System with Dynamic Policy Routing

A sophisticated Interactive Voice Response (IVR) system built using a multi-agent architecture with dynamic policy routing capabilities. This project demonstrates advanced conversational AI techniques including intent recognition, context management, and policy-based task execution.

## 🎯 Project Overview

This system implements a customer service automation solution using multiple specialized AI agents that work together to handle various customer service scenarios. The architecture showcases modern patterns in conversational AI, including:

- **Intent-based routing** with multi-level intent classification (L1/L2/L3)
- **Dynamic policy switching** for different service types
- **Multi-agent orchestration** with seamless handoffs
- **Context-aware conversation management**

## 🏗️ Architecture

The system consists of two main types of agents:

### 1. Orchestrator Agent
- **Primary Role**: Intent recognition and routing
- **Responsibilities**:
  - Maps user utterances to appropriate intent levels
  - Handles intent disambiguation through clarifying questions
  - Routes conversations to specialized fulfillment agents
  - Escalates to human agents when necessary

### 2. Fulfillment Agent
- **Primary Role**: Task execution based on dynamic policies
- **Responsibilities**:
  - Executes specific customer service workflows
  - Collects required information from users
  - Makes API calls to backend services
  - Handles error cases and edge scenarios

### Agent Communication Flow

```
User Input
    ↓
Orchestrator Agent (Intent Recognition)
    ↓
Policy Selection & Transfer
    ↓
Fulfillment Agent (Task Execution)
    ↓
Transfer back to Orchestrator OR Escalate to Human
```

## 🔧 Components

### Core Files

- **`agents.py`**: Defines agent configurations and transfer logic
- **`routines.py`**: Contains policy definitions and agent instructions
- **`tools.py`**: Mock API functions simulating backend services
- **`swarm/`**: Core multi-agent framework implementation

### Supported Policies

1. **Address Update Policy**
   - Validates current address
   - Collects new address information
   - Provides confirmation number

2. **Transaction Status Policy**
   - Retrieves transaction history
   - Handles single and multi-account scenarios
   - Provides transaction status details

3. **Account Balance Policy**
   - Fetches account balances
   - Supports multiple account types
   - Provides detailed balance information

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (for the underlying LLM)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd workshop_agentic_demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Running the System

```bash
python agents.py
```

The system will start an interactive REPL where you can interact with the IVR system.

## 💡 Example Interactions

### Simple Intent
```
User: "I need to check my balance"
System: [Routes to account_balance policy]
        "I'll help you check your account balance..."
```

### Ambiguous Intent
```
User: "I need to check something about my account"
System: "I'd be happy to help. Could you please specify what you'd like to check?"
        Options: Account balance, Transaction status, etc.
```

### Multi-step Transaction
```
User: "What's the status of my transaction?"
System: "When did the transaction occur?"
User: "Yesterday"
System: [Fetches account details]
        [Retrieves transaction history]
        "I found the following transactions..."
```

## 🛠️ Technical Highlights

### Dynamic Policy Assignment
The system uses a mapping-based approach to dynamically assign policies and functions to agents:

```python
INTENT_TO_POLICY_MAP = {
    'update_address': {
        'POLICY': UPDATE_ADDRESS_POLICY,
        'FUNCTIONS': [change_address]
    },
    # ... more policies
}
```

### Context Management
Agents maintain context across conversation turns, enabling:
- Seamless agent transfers
- State preservation during handoffs
- Multi-turn dialogue handling

### Extensibility
New policies can be added by:
1. Defining the policy instructions
2. Implementing required tool functions
3. Adding to the intent-to-policy mapping

## 📊 Skills Demonstrated

- **Multi-agent Systems**: Orchestration of multiple specialized agents
- **Natural Language Processing**: Intent classification and entity extraction
- **Conversation Design**: Multi-turn dialogue management
- **Software Architecture**: Modular, extensible system design
- **API Integration**: Mock backend service integration
- **Error Handling**: Graceful degradation and escalation strategies

## 🔮 Future Enhancements

- Add support for voice input/output
- Implement persistent conversation history
- Add analytics and monitoring capabilities
- Extend to support more service types
- Add automated testing suite
- Implement real backend API integrations

## 📝 License

MIT License - See LICENSE file for details

## 🎓 Academic Context

This project was developed as part of a graduate-level workshop on agentic AI systems, demonstrating practical applications of:
- Large Language Model orchestration
- Prompt engineering techniques
- Conversational AI design patterns
- Multi-agent system architecture

---

**Note**: This is a demonstration project using mock data and simulated API calls. In a production environment, these would be replaced with real backend services and proper authentication/security measures.
