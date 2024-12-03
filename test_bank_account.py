from bank_account import Bank_account

def test_bank_account_creation_and_get():
    test_case = Bank_account(balance = 2000.0, owner = "John Smith")
    assert test_case.get_balance() == 2000.0
    assert test_case.get_owner() == "John Smith"

def test_default_case():
    test_case = Bank_account("John Smith")
    assert test_case.get_balance() == 0
    assert test_case.get_owner() == "John Smith"

def test_set_owner():
    test_case = Bank_account("John Smith")
    test_case.set_owner("John Smitherson")
    assert test_case.get_owner() == "John Smitherson"

def test_deposit():
    test_case = Bank_account("John Smith")
    test_case.deposit(500)
    assert test_case.get_balance() == 500

def test_withdraw():
    test_case = Bank_account(balance = 5000, owner = "John Smith")
    test_case.withdraw(1000)
    assert test_case.get_balance() == 4000

def test_withdraw_too_large():
    test_case = Bank_account(balance = 100, owner = "John Smith")
    assert test_case.withdraw(200) == "Insufficient funds."