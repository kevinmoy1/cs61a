# CS 61A Fall 2014
# Name: Arani Bhattacharyay 
# Login: cs61a-aoy

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock < 1:
            return "Machine is out of stock."
        elif self.balance < self.price:
            diff = self.price - self.balance
            return "You must deposit ${0} more.".format(diff)
        else:
            self.stock -= 1
            change = self.balance - self.price
            self.balance = 0
            if change > 0:
                return "Here is your {0} and ${1} change.".format(self.product, change)
            else:
                return "Here is your {0}.".format(self.product)

    def deposit(self, amount):
        if self.stock < 1:
            return "Machine is out of stock. Here is your ${0}.".format(amount)
        else:
            self.balance += amount
            return "Current balance: ${0}".format(self.balance)

    def restock(self, stock):
        self.stock += stock
        return "Current {0} stock: {1}".format(self.product, self.stock)

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, vendor):
        self.vendor = vendor

    def ask(self, message, *args):
        if "please" in message:
            call = message[7:]
            if hasattr(self.vendor, call):
                return getattr(self.vendor, call)(*args)
            else:
                return "Thanks for asking, but I know not how to {0}".format(call)
        else:
            return "You must learn to say please first."

