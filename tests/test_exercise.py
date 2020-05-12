import pytest
from src.payment_card import PaymentCard

def test_exercise(capsys):
    card = PaymentCard(30)
    print(card)

    out, err = capsys.readouterr()
    assert out == "The card has a balance of 30 pounds\n"

    card.eat_affordably()
    print(card)

    out, err = capsys.readouterr()
    assert out == "The card has a balance of 27.4 pounds\n"

    card.eat_heartily()
    card.eat_affordably()
    print(card)

    out, err = capsys.readouterr()
    assert out == "The card has a balance of 20.199999999999996 pounds\n"

    card = PaymentCard(10)
    card.add_money(15)
    print(card)

    out, err = capsys.readouterr()
    assert out == "The card has a balance of 25 pounds\n"
