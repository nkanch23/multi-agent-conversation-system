import random, string, uuid

# Helper data
account_types = ["IRA", "BROKERAGE", "RETIREMENT"]
transaction_types = ["BUY", "SELL", "TRANSFER", "DIVIDEND"]
transaction_statuses = ["COMPLETED", "PENDING", "POSTED", "CANCELLED"]

# Helper function to generate a random confirmation number
def generate_random_confirmation_number():
    return f"WA{random.randint(10000000, 99999999)}"

# Function for 'validate_address'
def change_address(address='', city='', state='', zipcode=''):
    """
    Mock function to simulate validating and standardizing the input address.
    
    Args:
        address (str): The address to validate.
        city (str): The city of the address.
        state (str): The state of the address.
        zipcode (str): The zipcode of the address.

    Returns:
        dict: A dictionary containing the standardized address and additional details.
    """
    response = {
        "confirmationNumber": generate_random_confirmation_number()
    }
    return response

# Helper function to pick random elements from a list
def get_random_elements(elements, count=1):
    return random.sample(elements, count)

# Helper function to generate random account IDs
def generate_random_account_id():
    return ''.join(random.choices(string.digits, k=15))

# Helper function to generate random transaction IDs
def generate_random_transaction_id():
    return ''.join(random.choices(string.digits, k=9))

def get_all_acct_details():
    """
    Mock function to retrieve random account details, like account type and account IDs.

    Returns:
        dict: A dictionary containing random account types and account IDs.
    """
    response = {
        "account_type": get_random_elements(account_types, random.randint(1, 3)),  # Random 1-3 account types
        "account_ids": [generate_random_account_id() for _ in range(random.randint(2, 5))]  # Random 2-5 account IDs
    }
    return response

def get_transaction_history(transaction_date='', account_ids=''):
    """
    Mock function to retrieve random transaction history based on account IDs and position IDs.

    Args:
        transaction_date (str): The date of the transactions.
        account_ids (list): A list of account IDs to retrieve transactions for.

    Returns:
        dict: A dictionary containing random transaction details.
    """
    
    # Mocking transactions for each account_id
    transactions = []
    for _ in [generate_random_account_id() for _ in range(random.randint(1, 2))]:
        transaction = {
            "transaction_id": [generate_random_transaction_id() for _ in range(random.randint(0,1))],  # Random 1-3 transaction IDs
            "transaction_type": get_random_elements(transaction_types, 1),  # Random 1-2 transaction types
            "transaction_status_code": get_random_elements(transaction_statuses, 1)  # Random 1-3 statuses
        }
        transactions.append(transaction)

    response = {
        "transactions": transactions
    }
    return response

# Helper function to generate random balances
def generate_random_balances():
    return [round(random.uniform(1000, 100000), 2) for _ in range(3)]

# Helper function to pick random elements from a list
def get_random_elements(elements, count=1):
    return random.sample(elements, count)

def get_all_acct_balances():
    """
    Mock function to retrieve account details, including account types and random balances.

    Returns:
        dict: A dictionary containing account types and corresponding random balances.
    """
        
    # Generate random balances for each account type
    balances = generate_random_balances()
    
    response = {
        "account_type": get_random_elements(account_types, random.randint(1, 3)),
        "balances": balances
    }
    return response

