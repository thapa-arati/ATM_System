class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is {self.balance}$")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}$ deposited successfully.")
        self.check_balance()

    def withdraw(self, amount):
        if amount < 20:
            print("Amount should be greater or equal to $20 ")
        else:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount}$ withdrawn successfully.")
            else:
                print("Insufficient funds.")
            self.check_balance()


def authenticate_pin():
    pin = input("\nEnter your 4-digit PIN: ")
    if len(pin) != 4:
        print("PIN should be exactly 4 digits.")
        return False
    elif not pin.isdigit():
        print("PIN should contain only numeric digits.")
        return False
    else:
        # Assume the correct PIN is '1234'
        if pin == '1234':
            print("Hi! Arati Thapa.\nWelcome To Our ATM Service.")
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False


def main():
    print("Welcome to the ATM!")
    while True:
        print("\n**** ATM Menu ****")
        print("1. Insert Card")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            if authenticate_pin():
                atm = ATM()  # Create an instance of the ATM class
                while True:
                    print("\n**** ATM Menu ****")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Exit")
                    inner_choice = input("Enter your choice (1-4): ")

                    if inner_choice == '1':
                        atm.check_balance()
                    elif inner_choice == '2':
                        amount = float(input("Enter the amount to deposit: "))
                        atm.deposit(amount)
                    elif inner_choice == '3':
                        amount = float(input("Enter the amount to withdraw: "))
                        atm.withdraw(amount)
                    elif inner_choice == '4':
                        print("******Please take your receipt*****\nThank you for using our ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                break
        elif choice == '2':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
