# CS 61A Fall 2014
# Name: Arani Bhattacharyay
# Login: cs61a-aoy

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n<= 3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)
        

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    first_term, second_term, third_term = 1,2,3
    if n == first_term:
        return first_term 
    elif n == second_term:
            return second_term 
    elif n == third_term:
            return third_term
    else:
        ind = 3
        while ind < n:
            this_term = third_term + 2 * second_term + 3*first_term
            first_term = second_term
            second_term = third_term
            third_term = this_term
            ind+=1
    return this_term          

      


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k%10 == 7:
        return True
    elif k == 0:
        return False
    else: 
        return has_seven(k//10) 

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def count_up(term, stopper):
        if stopper == n:
            return term
        if stopper%7 == 0 or has_seven(stopper):
            return count_down(term-1, stopper+1)
        return count_up(term+1,stopper+1)
    def count_down(term, stopper):
        if stopper == n:
            return term        
        if stopper%7 == 0 or has_seven(stopper):
            return count_up(term+1, stopper+1)
        return count_down(term-1, stopper+1)
    return count_up(1,1)    

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def coin_list(amount):
        index = 0
        i = []
        while 2**index < amount:
            i.append(2**index)
            index+=1
        return i
    
    lst = coin_list(amount)
    lst.reverse()
    

    def changer(amount, lst):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif len(lst) == 0:
            return 0
        else:
            return changer(amount-lst[0], lst) +  changer(amount, lst[1:]) 
        
    return changer(amount, lst)


        
def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    
    def printer(start, end):
        print("Move the top disk from rod", start, "to rod", end)
        
    def moverod(n, start, end, extra):
        if n == 1:
            printer(start, end)
            return
        moverod(n - 1, start, extra, end)
        printer(start, end)
        moverod(n - 1, extra, end, start)
    moverod(n, start, end, 2)
    
    
    

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return lambda l : (lambda f,g:f(f,g)) ( (lambda f,x: 1 if x == 0 else x * f(f,x-1)) ,l)


