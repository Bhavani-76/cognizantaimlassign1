from src.models.abc_banking_group import ABCBankingGroup
from src.models.savings_account import SavingsAccount

def test_add_account():
    bank = ABCBankingGroup()
    acc = SavingsAccount(10000, "01-01-2025", 5)

    bank.add_account(acc)

    assert len(bank.accounts) == 1