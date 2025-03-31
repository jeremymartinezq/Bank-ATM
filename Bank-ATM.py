import random


# Parent Class
class Account:
   def __init__(self, account_holder, account_type, credit_score, annual_income, balance=0.0):
       # Initialize common account attributes
       self.account_holder = account_holder
       self.account_type = account_type
       self.credit_score = credit_score
       self.annual_income = annual_income
       self.balance = balance


   def account_detail(self):
       # Print the information of attributes of the constructor
       print(f"Account Holder: {self.account_holder}")
       print(f"Account Type: {self.account_type}")
       print(f"Credit Score: {self.credit_score}")
       print(f"Annual Income: ${self.annual_income:.2f}")
       print(f"Balance: ${self.balance:.2f}")


# Child Class for Debit
class Debit(Account):
   def __init__(self, account_holder, account_type, credit_score, annual_income, balance=0.0):
       super().__init__(account_holder, account_type, credit_score, annual_income, balance)
       self.account_number = random.randint(444400000000, 444499999999)


   def deposit(self, amount):
       self.balance += amount
       print(f"${amount:.2f} deposited.")


   def withdraw(self, amount):
       if amount > self.balance:
           print("Insufficient balance.")
       else:
           self.balance -= amount
           print(f"${amount:.2f} withdrawn.")


   def check_balance(self):
       print(f"Current Balance: ${self.balance:.2f}")


   def account_detail(self):
       super().account_detail()
       print(f"Account Number: {self.account_number}")
       print(f"Balance: ${self.balance:.2f}")


# Child Class for Credit
class Credit(Account):
   def __init__(self, account_holder, account_type, credit_score, annual_income):
       super().__init__(account_holder, account_type, credit_score, annual_income)
       self.account_number = random.randint(555500000000, 555599999999)
       self.credit_limit = self.calculate_credit_limit()


   def calculate_credit_limit(self):
       if 580 <= self.credit_score <= 669 and self.annual_income >= 60000:
           return 1000
       elif 670 <= self.credit_score <= 739 and self.annual_income >= 80000:
           return 2000
       elif self.credit_score >= 740 and self.annual_income >= 100000:
           return 4000
       return 500


   def make_purchase(self, purchase_amount):
       if self.balance + purchase_amount > self.credit_limit:
           print("Purchase exceeds credit limit.")
       else:
           self.balance += purchase_amount
           print(f"Purchase of ${purchase_amount:.2f} made.")


   def withdraw(self, amount):
       withdrawal_fee = amount * 0.05
       total_amount = amount + withdrawal_fee
       if total_amount > self.credit_limit:
           print("Withdrawal exceeds credit limit.")
       elif total_amount > self.balance:
           print("Insufficient balance.")
       else:
           self.balance -= total_amount
           print(f"${amount:.2f} withdrawn. Fee: ${withdrawal_fee:.2f}")


   def pay_credit(self, payment_amount):
       self.balance -= payment_amount
       print(f"${payment_amount:.2f} payment made.")


   def check_balance(self):
       print(f"Current Balance: ${self.balance:.2f}")


   def account_detail(self):
       super().account_detail()
       print(f"Account Number: {self.account_number}")
       print(f"Credit Limit: ${self.credit_limit:.2f}")
       print(f"Balance: ${self.balance:.2f}")


# Menu Function
def transaction_menu(account):
   while True:
       print("\nMenu:")
       print("1. Account Details")
       print("2. Check Balance")
       if isinstance(account, Debit):
           print("3. Deposit")
           print("4. Withdraw")
       elif isinstance(account, Credit):
           print("5. Make a Purchase")
           print("6. Withdraw from Credit Card")
           print("7. Make a Payment to Your Credit Card")
       print("8. Exit")


       # User inputs their choice from the menu
       choice = int(input("Enter your choice: "))


       # Perform actions based on user choice
       if choice == 1:
           account.account_detail()
       elif choice == 2:
           account.check_balance()
       elif isinstance(account, Debit):
           if choice == 3:
               amount = float(input("Enter deposit amount: "))
               account.deposit(amount)
           elif choice == 4:
               amount = float(input("Enter withdrawal amount: "))
               account.withdraw(amount)
       elif isinstance(account, Credit):
           if choice == 5:
               amount = float(input("Enter purchase amount: "))
               account.make_purchase(amount)
           elif choice == 6:
               amount = float(input("Enter withdrawal amount: "))
               account.withdraw(amount)
           elif choice == 7:
               amount = float(input("Enter payment amount: "))
               account.pay_credit(amount)
       elif choice == 8:
           # Print transaction summary on exit
           transaction_number = random.randint(10000, 1000000)
           print("\nTransaction Summary:")
           print(f"Transaction Number: {transaction_number}")
           print(f"Account Holder: {account.account_holder}")
           print(f"Account Number: {account.account_number}")
           print(f"Account Balance: ${account.balance:.2f}")
           break
       else:
           print("Invalid choice. Please try again.")


       # Ask user if they want to perform another transaction
       continue_transaction = input("Do you want to do any other transaction? (y/n): ").lower()
       if continue_transaction != 'y':
           transaction_number = random.randint(10000, 1000000)
           print("\nTransaction Summary:")
           print(f"Transaction Number: {transaction_number}")
           print(f"Account Holder: {account.account_holder}")
           print(f"Account Number: {account.account_number}")
           print(f"Account Balance: ${account.balance:.2f}")
           break


# Main Program
if __name__ == "__main__":
   # Collect user information
   account_holder = input("Enter your name: ")
   account_type = input("Enter your account type: (Please type either credit or debit) ").lower()
   credit_score = int(input("Enter your credit score: "))
   annual_income = float(input("Enter your annual income: $"))


   # Create an account based on the type provided by the user
   if account_type == "debit":
       account = Debit(account_holder, account_type, credit_score, annual_income)
   elif account_type == "credit":
       account = Credit(account_holder, account_type, credit_score, annual_income)
   else:
       print("Invalid account type entered.")
       exit()


   # Call the menu function to start transactions
   transaction_menu(account)



