import mysql.connector as sql

mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database = 'transaction_tracker')

mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE transaction_tracker")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#      print(db)

# mycursor.execute("CREATE TABLE users_table(id INT(3) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, phone_number VARCHAR(11) UNIQUE, username VARCHAR(50), password VARCHAR(50) )")

# mycursor.execute("SHOW TABLES")
# for db in mycursor:
#     print(db)

import mysql.connector
import datetime
import time
import sys



# Create a MySQL database connection
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='bank_app'
)

def add_transaction(beneficiary, transaction_type, amount):
    cursor = conn.cursor()

    # Insert a new transaction into the database
    transaction_date = datetime.datetime.now()
    insert_query = '''
        INSERT INTO transaction_table (beneficiary, transaction_type, amount, date_time)
        VALUES (%s, %s, %s, %s)
    '''
    data = (beneficiary, transaction_type, amount, transaction_date)
    cursor.execute(insert_query, data)
    
    # Commit the transaction and close the cursor
    conn.commit()
    cursor.close()

def get_user_information(account_number):
    cursor = conn.cursor()

    # Retrieve user information for the specified account number
    select_query = '''
        SELECT * FROM customer_table
        WHERE account_no = %s
    '''
    cursor.execute(select_query, (account_number,))
    user_information = cursor.fetchone()
    
    # Close the cursor
    cursor.close()

    return user_information

def get_all_transactions(beneficiary):
    cursor = conn.cursor()

    # Retrieve all transactions for the specified beneficiary
    select_query = '''
        SELECT transaction_id, beneficiary, transaction_type, amount, date_time
        FROM transaction_table
        WHERE beneficiary = %s
    '''
    cursor.execute(select_query, (beneficiary,))
    transactions = cursor.fetchall()
    
    # Close the cursor
    cursor.close()

    return transactions

if __name__ == '__main__':
    class Page:
        def __init__(self, name):
            self.name = name
            self.main()

        def main(self):
            self.page1()

        def page1(self):
            time.sleep(1)
            print(f'''
            
                                                                            Welcome to {self.name}
            ''')
            time.sleep(2)
            print("""
                                                                                        1. Log in
                                                                                        2. Sign up
                                                                                        3. Help
                                                                                        4. Exit
            """)

            while True:
                user = input('\nUser: ')

                if user == "1":
                    self.log_in()
                    break
                elif user == "2":
                    self.sign_up()
                    break
                elif user == "3":
                    self.help1()
                    break
                elif user == "4":
                    self.exit()
                    break
                else:
                    print("\nInvalid input! Please try again.")


                                                                # SIGN UP


        def sign_up(self):
            query = "INSERT INTO users_table(fullname, email, phone_number, username, password) VALUES(%s,%s,%s,%s,%s)"
            time.sleep(1)
            print('''
                                                                                        Sign up page
            ''')
            self.fullname = input(f"\nFullname: ")
            time.sleep(1)
            self.email_address = input("\nEmail address: ")
            time.sleep(1)
            self.phone_number = input("\nPhone number: ")
            time.sleep(1)
            self.username = input("\nUsername: ")
            time.sleep(1)
            self.password = input(f"\nPassword: ")
            time.sleep(1)
            val = (self.fullname, self.email_address, self.phone_number, self.username, self.password)
            mycursor.execute(query, val)
            mycon.commit()
            # print(mycursor.rowcount, 'row inserted successfully')
            print('\nPlease wait...')
            time.sleep(2)
            print("\nLoading...")
            time.sleep(3)
            print("\nSuccessfully registered")
            self.log_in()


                                                                # Log in


        def log_in(self):
            query = "SELECT username, password FROM users_table WHERE username = %s AND password = %s"
            time.sleep(1)
            print('''
                                                                                        Log in page
            ''')
            self.username = input("\nUsername: ")
            time.sleep(1)
            self.password = input(f"\nPassword: ")
            time.sleep(1)
            val = (self.username, self.password)
            mycursor.execute(query, val)
            output = mycursor.fetchall()
            if output:
                print('\nPlease wait...')
                time.sleep(1.5)
                print("\nLoading...")
                time.sleep(2)
                self.home_page()
            else:
                print(f"\nWrong password or username!")
                user = input("\nPress 'a' to reset password, 'b' to reset username or 'c' to sign up: ")



                                                    # For password


                
                time.sleep(1)
                print("""
                                                                                    Reset Password/username
                """)                    

                if user.lower() == "a":
                    time.sleep(1)
                    email = input("\nEnter your Email: ")
                    time.sleep(1)
                    query1 = ("SELECT email, password FROM users_table WHERE email=%s")
                    val1 = (email,)
                    mycursor.execute(query1, val1)
                    detail = mycursor.fetchall()

                    if detail:
                        while True:
                            self.password = input("\nEnter your new password: ")
                            time.sleep(1)
                            self.confirm_password = input("\nConfirm your new password: ")

                            if self.password == self.confirm_password:
                                query = 'UPDATE users_table SET password = %s WHERE email = %s'
                                val =(self.confirm_password, email)
                                mycursor.execute(query,val)
                                mycon.commit()
                                time.sleep(1)
                                print("\nPassword reset successfully.")
                                self.log_in()
                                break
                            else:
                                print("\nPassword do not match! Please try again.")
                    else:
                        time.sleep(1)
                        print('\nWrong email address')
                        self.log_in()


                                            # For Username
                elif user.lower() == "b":
                    time.sleep(1)
                    email = input("\nEnter your Email: ")
                    time.sleep(1)
                    query1 = ("SELECT email, username FROM users_table WHERE email=%s")
                    val1 = (email,)
                    mycursor.execute(query1, val1)
                    detail = mycursor.fetchall()

                    if detail:
                        while True:
                            user_name = input("\nEnter your new username: ")
                            time.sleep(1)
                            confirm_username = input("\nConfirm your new username: ")

                            if user_name == confirm_username:
                                query = 'UPDATE users_table SET username = %s WHERE email = %s'
                                val = (confirm_username, email)
                                mycursor.execute(query, val)
                                mycon.commit()
                                print("\nUsername changed successfully.")
                                self.log_in()
                                break 
                            else:
                                print("\nUsernames do not match! Please try again.")

                                            
                    elif user.lower() == "c":
                        self.sign_up()



        def home_page(self):
            time.sleep(2)
            val = (self.username, self.password)
            while True:
                time.sleep(1)
                print(f"""
                                                                                        Welcome {self.username}
                    """)
                print("""
                                                                    1. Add Transaction                  3. Get User Information
                                                                    2. Get All Transactions             4. Help
                                                                    5. Exit
                    """)
                choice = input("\nEnter your choice: ")

                if choice == '1':
                    time.sleep(1)
                    print("""
                                                                                    Add Transaction
                        """)
                    time.sleep(0.5)
                    beneficiary = input("\nEnter the account number: ")
                    time.sleep(0.5)
                    transaction_type = input("\nEnter transaction type: ")
                    time.sleep(0.5)
                    amount = float(input("\nEnter amount: "))
                    time.sleep(1.5)
                    add_transaction(beneficiary, transaction_type, amount)
                    print("\nTransaction added successfully.\n")

                elif choice == '2':
                    time.sleep(1)
                    print("""
                                                                                    Get All Transaction
                        """)
                    time.sleep(0.5)
                    beneficiary = input("\nEnter the account number: ")
                    time.sleep(1)
                    transactions = get_all_transactions(beneficiary)
                    print("\nAll Transactions:")
                    time.sleep(1.5)
                    for transaction in transactions:
                        print(f"\nID: {transaction[0]},\n \nAccount number: {transaction[1]},\n \nType: {transaction[2]},\n \nAmount: {transaction[3]},\n \nDate: {transaction[4]}")
                    print()

                elif choice == '3':
                    time.sleep(1)
                    print("""
                                                                                    Get User Information
                        """)
                    time.sleep(0.5)
                    account_number = input("\nEnter account number: ")
                    time.sleep(1.5)
                    user_information = get_user_information(account_number)
                    if user_information:
                        print("\nUser Information:")
                        print(f"\nUser ID: {user_information[0]}")
                        print(f"\nName: {user_information[1]}")
                        print(f"\nEmail: {user_information[2]}")
                        print(f"\nPhone number: {user_information[3]}")
                        print(f"\nBVN: {user_information[4]}")
                        print(f"\nUsername: {user_information[5]}")
                        print(f"\nPassword: {user_information[6]}")
                        print(f"\nAccount number: {user_information[7]}")
                        print(f"\nAccount balance: {user_information[8]}")
                        print()
                    else:
                        print("User not found.\n")

                elif choice == '4':
                    time.sleep(1)
                    print("""
                                                                                                    Help
                    """)
                    time.sleep(1)
                    print("""
                                                                                                1. Contact us
                                                                                                2. Email us
                                                                                                3. Chat with us
                    """)
                else:
                    print("\nInvalid input! Please try again.")


            conn.close()


tracker = Page('Transaction Tracker')