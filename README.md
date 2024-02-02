# Transaction Tracker

This Python script provides a simple transaction tracking system using MySQL as the backend database. Users can log in, sign up, add transactions, view all transactions, and retrieve user information.

## Requirements

- Python 3.x
- MySQL Connector (`pip install mysql-connector-python`)

## Setup

1. **MySQL Database:**
   - Make sure you have a MySQL server installed and running.
   - Create a database named `transaction_tracker` (or adjust the `database` parameter in the connection).
   - Uncomment the code to create the database and user table if needed.

2. **Dependencies:**
   - Install the required Python packages using the following command:
     ```
     pip install mysql-connector-python
     ```

3. **Run the Script:**
   - Run the script using Python:
     ```
     python transaction_tracker.py
     ```

## Functionality

### MySQL Database Connection

- Establishes a connection to the MySQL database with the specified parameters.

### Transaction Functions

- `add_transaction(beneficiary, transaction_type, amount)`: Adds a new transaction to the database.
- `get_user_information(account_number)`: Retrieves user information based on the account number.
- `get_all_transactions(beneficiary)`: Retrieves all transactions for a specified beneficiary.

### User Interface

- The script includes a simple command-line interface allowing users to:
  - Log in or sign up.
  - Add transactions with details like beneficiary, transaction type, and amount.
  - View all transactions for a specified beneficiary.
  - Retrieve user information based on the account number.

## Usage

1. Run the script and follow the on-screen instructions.
2. Log in or sign up to access transaction-related functionalities.
3. Add transactions, view transaction history, and retrieve user information.

## Note

- This script serves as a basic transaction tracking system and is intended for educational purposes.
- Ensure to secure your MySQL database by setting strong passwords and configuring appropriate access permissions.

Feel free to customize and enhance the script based on your specific requirements.

For any questions or issues, please refer to the MySQL Connector documentation or seek assistance from the community.
