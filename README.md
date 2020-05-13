# Exercise 4.16 Payment Card

In this exercise series, a class called `PaymentCard` is created which aims to mimic a payment process.

## The class template

The project will include two code files:

The exercise template comes with a code file called `main.py`, which contains the `main` method.

Add a new class to the project called `PaymentCard`. This can be done by adding a file called `payment_card.py` in the `src` directory.

First, create the `PaymentCard` object's constructor, which is passed the opening balance of the card, and which then stores that balance in the object's internal variable. Then, write the `__str__` method, which will return the card's balance in the form "The card has a balance of X pounds".

The following is the template of the `PaymentCard` class:


```python
class PaymentCard:
    def __init__(self, opening_balance):
        # write code here

    def __str__(self):
        # write code here
```

The following main program tests the class:

```python
def main():
    card = PaymentCard(50)
    print(card)
```

The program should print the following:

```plaintext
The card has a balance of 50.0 pounds
```

## Making transactions

Complement the `PaymentCard` class with the following methods:

```python
def eat_affordably(self):
    # write code here

def eat_heartily(self):
    # write code here
```

The method `eat_affordably` should reduce the card's balance by £2.60, and the method `eat_heartily` should reduce the card's balance by £4.60.

The following main program tests the class:

```python
def main():
    card = PaymentCard(50)
    print(card)

    card.eat_affordably()
    print(card)

    card.eat_heartily()
    card.eat_affordably()
    print(card)
```

The program should print approximately the following:

```plaintext
The card has a balance of 50.0 pounds
The card has a balance of 47.4 pounds
The card has a balance of 40.199999999999996 pounds
```

## Non-negative balance

What happens if the card runs out of money? It doesn't make sense in this case for the balance to turn negative. Change the methods `eat_affordably` and `eat_heartily` so that they don't reduce the balance should it turn negative.

The following main program tests the class:

```python
def main():
    card = PaymentCard(5)
    print(card)

    card.eat_heartily()
    print(card)

    card.eat_heartily()
    print(card)
```

The program should print the following:

```plaintext
The card has a balance 5.0 pounds
The card has a balance 0.40000000000000036 pounds
The card has a balance 0.40000000000000036 pounds
```

The second call to the method `eat_heartily` above did not affect the balance, since the balance would have otherwise become negative.

## Topping up the card

Add the following method to the `PaymentCard` class:

```python
def add_money(self,amount):
    # write code here
```

The purpose of the method is to increase the card's balance by the amount of money given as a parameter. However, the card's balance may not exceed 150 pounds. As such, if the amount to be topped up exceeds this limit, the balance should, in any case, become exactly 150 pounds.

The following main program tests the class:

```python
def main():
    card = PaymentCard(10)
    print(card)

    card.add_money(15)
    print(card)

    card.add_money(10)
    print(card)

    card.add_money(200)
    print(card)
```

The program should print the following:

```plaintext
The card has a balance of 10.0 pounds
The card has a balance of 25.0 pounds
The card has a balance of 35.0 pounds
The card has a balance of 150.0 pounds
```

## Topping up the card with a negative value

Change the `add_money` method further, so that if there is an attempt to top it up with a negative amount, the value on the card will not change.

The following main program tests the class:

```python
def main():
    card = PaymentCard(10)
    print("Paul: " + str(card))
    card.add_money(-15)
    print("Paul: " + str(card))
```

The program should print the following:

```plaintext
Paul: The card has a balance of 10.0 pounds
Paul: The card has a balance of 10.0 pounds
```

## Multiple cards

Write code in the `main` method of the exercise.py file that contains the following sequence of events:

- Create Paul's card. The opening balance of the card is 20 pounds
- Create Matt's card. The opening balance of the card is 30 pounds
- Paul eats heartily
- Matt eats affordably
- The cards' values ​​are printed (each on its own line, with the cardholder name at the beginning of it)
- Paul tops up 20 pounds
- Matt eats heartily
- The cards' values ​​are printed (each on its own line, with the cardholder name at the beginning of it)
- Paul eats affordably
- Paul eats affordably
- Matt tops up 50 pounds
- The cards' values ​​are printed (each on its own line, with the cardholder name at the beginning of it)

The main program's template is as follows:

```python
def main():
    pauls_card = PaymentCard(20)
    matts_card = PaymentCard(30)

    # write code here
```

The program should produce the following print output:

```plaintext
Paul: The card has a balance of 15.4 pounds
Matt: The card has a balance of 27.4 pounds
Paul: The card has a balance of 35.4 pounds
Matt: The card has a balance of 22.799999999999997 pounds
Paul: The card has a balance of 30.199999999999996 pounds
Matt: The card has a balance of 72.8 pounds
```
