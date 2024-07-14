accounts = {}

def create_account():
    acc_num = input("Enter the account number you want: ")
    acc_name = input("Enter your name: ")
    accounts[acc_num] = {'holder': acc_name, 'balance': 0}
    print("Account created.")

def deposit_money():
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        amount = float(input("Enter the amount to deposit: "))
        accounts[acc_num]['balance'] += amount
        print(f"Rs.{amount} deposited. New balance: Rs.{accounts[acc_num]['balance']}")
    else:
        print("Account not found.")

def delete_account():
    acc_num = input("Enter the account number to delete: ")
    if acc_num in accounts:
        del accounts[acc_num]
        print("Account deleted.")
    else:
        print("Account not found.")

def view_account():
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        account = accounts[acc_num]
        print(f"Account Number: {acc_num}, Account Holder: {account['holder']}, Balance: Rs.{account['balance']}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Deposit Money")
        print("4. View Account")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            delete_account()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            view_account()
        elif choice == '5':
            print("Thank you for using the bank management system!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
