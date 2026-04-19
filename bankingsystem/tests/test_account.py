from src.models.savings_account import SavingsAccount
from src.models.current_account import CurrentAccount

def test_savings_account():
    sa = SavingsAccount(10000, "01-01-2025", 5)
    assert sa.running_total == 10000
    assert sa.interest_rate == 5

def test_current_account():
    ca = CurrentAccount(20000, "02-01-2025", 1000)
    assert ca.running_total == 20000
    assert ca.overdraft_limit == 1000