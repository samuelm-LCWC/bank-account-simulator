# Bank Account Simulator
Create a class called Bank_account to simulate bank account operations. The class will have the following attributes:

* Balance - default value of zero (but can start as any other non-negative value)
* Owner

You will also have three methods that can be carried out:

* deposit
* withdraw
* get_balance
 

## Examples
```
account = BankAccount("Alice")
print(account.owner)          # ➞ "Alice"
print(account.get_balance())  # ➞ 0

account.deposit(100)
print(account.get_balance())  # ➞ 100

account.withdraw(50)
print(account.get_balance())  # ➞ 50

account.withdraw(100)         # ➞ "Insufficient funds"
print(account.get_balance())  # ➞ 50
```

### Note:
You will __need__ to make use of a default parameter value here to allow the balance to default to zero, refer to this <a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">W3Schools</a> page for more information
