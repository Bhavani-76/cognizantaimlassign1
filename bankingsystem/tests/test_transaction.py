from src.models.direct_debit import DirectDebit

def test_transaction():
    t = DirectDebit(5000, "10AM", "A", "B", "05-05-2025")

    assert t.amount == 5000
    assert t.sender == "A"
    assert t.receiver == "B"