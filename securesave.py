# ----------------------------------------------------------------------------------
# -------------------------- SecureSave App. ---------------------------------------
# ----------------------------------------------------------------------------------

#defining variables ----------------------------------------------------------------

all_accounts = {}
num_of_account = 1000

# Account Creation ------------------------------------------------------------------

def create_account():
    global num_of_account
    cust_name = input("Enter your full name: ")
    cust_phone = input("Enter your phone number: ")
    cust_dob = input("Enter your date of birth(DD-MM-YYYY): ")
    cust_age = input("Enter your age: ")
    cust_gender = input("Are you male or female: ")
    cust_email = input("Enter your email: ")

    generated_acct_num = num_of_account + 1
    num_of_account = num_of_account + 1

    account_details = {
            "acct_num": generated_acct_num,
            "balance": 0,
            "cust_name": cust_name,
            "phone_num": cust_phone,
            "dob": cust_dob,
            "age": cust_age,
            "gender": cust_gender,
            "email": cust_email,
            "history": []
            }
    
    all_accounts[generated_acct_num] = account_details
    print(f"Account created successfully!\n- Account name: {cust_name}\n- Account No.:{generated_acct_num}\n- Current Balance: 0")


# Deposit Function ----------------------------------------------------------------------------------

def do_deposit():
    # print(all_accounts)
    acct_num = int(input("What is your account number?: "))
    deposit_amt = int(input("How much do you want to deposit?: "))

    current_balance = all_accounts[acct_num]["balance"]
    print(f"Initial balance: {current_balance}")
    all_accounts[acct_num]["balance"] += deposit_amt
    new_balance = all_accounts[acct_num]["balance"]
    print(f"You have just deposited {deposit_amt}, your new balance is {new_balance}")
    print(f"New balance: {new_balance}")
    # Logging to transaction history
    all_accounts[acct_num]["history"].append(f"You deposited: {deposit_amt}")
    # print(all_accounts[acct_num]["history"])


# Withdrawal Function -------------------------------------------------------------------------------

def do_withdrawal():
    # print(all_accounts)
    acct_num = int(input("What is your account number?: "))
    withdraw_amt = int(input("How much do you want to withdraw?: "))

    current_balance = all_accounts[acct_num]["balance"]
    print(f"Initial balance: {current_balance}")
    if current_balance >= withdraw_amt:
        all_accounts[acct_num]["balance"] -= withdraw_amt
        new_balance = all_accounts[acct_num]["balance"]
        print(f"You have just withdrawn {withdraw_amt}, your remaining balance is {new_balance}")

        # Logging to transaction history
        all_accounts[acct_num]["history"].append(f"You withdrew: {withdraw_amt}")
    else:
        print(f"Sorry! You have insufficient funds to withdraw.\nYou can only upto {current_balance}")
    print(f"New balance: {all_accounts[acct_num]["balance"]}")
    # print(all_accounts[acct_num]["history"])


# Check Balance Function ----------------------------------------------------------------------------

def check_balance():
    acct_num = int(input("What is your account number?: "))
    balance = all_accounts[acct_num]["balance"]
    print(f"Your current balance is {balance}")


# View Transaction History Function -----------------------------------------------------------------

def transaction_history():
    acct_num = int(input("What is your account number?: "))

    if len(all_accounts[acct_num]["history"]) != 0:
        print("----- Here's your full Transaction History -----\n")
        for history in all_accounts[acct_num]["history"]:  
            print(f"- {history}\n")
    else:
        print("--- You have not performed any transaction history yet! ---")


# Creating a Menu -----------------------------------------------------------------------------------

run_securesave_app = True

while run_securesave_app:
    print("\n----- Welcome to SecureSave Bank. ----- \nWhat would you like to do today?")

    customer_choice = int(input("Please enter the number corresponding to what you want to do.\n1. Create Account.\n2. Check Balance.\n3. Deposit.\n4. Withdrawal\n5. Transaction History\n6. Exit"))

    if customer_choice == 1:
        # Create account
        print("Creating your account...")
        create_account()
    elif customer_choice == 2:
        # Check Balance
        print("Checking your balance...")
        check_balance()
    elif customer_choice == 3:
        # Do deposit
        print("Depositing...")
        do_deposit()
    elif customer_choice == 4:
        #Do withdrawal
        print("Withdrawing...")
        do_withdrawal()
    elif customer_choice == 5:
        # Transaction History
        print("Checking your transaction history...")
        transaction_history()
    elif customer_choice == 6:
        run_securesave_app = False
    else:
        print("Wrong input, enter the correct option. Try again")
















