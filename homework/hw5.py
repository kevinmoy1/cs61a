# CS 61A Fall 2014
# Name: Arani Bhattacharyay
# Login: cs61a-aoy

def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    "*** YOUR CODE HERE ***"
    first_half = cards[:len(cards)//2]
    second_half = cards[len(cards)//2:]
    final = []
    counter = 0
    while counter < len(first_half):
        final.append(first_half[counter])
        final.append(second_half[counter])
        counter+=1
    return final

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    "*** YOUR CODE HERE ***"
    #assume first one is longer because it is in the doctests
    """first_total = first[0]
    second_total = second[0]
    indF, indS = 0,0
    while indF < len(first):
        while sun(first_total)<= sum(second_total):
            if first_total == second_total:
                first[:indF+1]
                second[:indS+1]
                first.insert(0,second_total)
                second.insert(0,first_total)
                return "Deal!"
            else:
                indF += 1
                first_total.append(first[indF])
        
        indS +=1
        second_total.append(second[indS])
    return "No Deal!" """
    

    def exchange (lst1, lst2):
        for i in range(len(lst1)):
            first.remove(lst1[i])
            if i < len(lst2):
                first.insert(i, lst2[i])
        for c in range(len(lst2)):
            second.pop(0)
        for d in range(len(lst1)):
            second.insert(d, lst1[d])

    possible_sums = []
    total = 0
    for i in range(len(first)):
        total += first[i]
        possible_sums.append(total)
    run = 0
    for i in range(len(second)):  
        run += second[i]
        if run in possible_sums:
            exchange(first[:possible_sums.index(run)+1], second[:i+1])
            return 'Deal!'

    return 'No deal!'  

            

################################
# Linked list data abstraction #
################################

empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6, empty))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3, empty))
    True
    >>> has_prefix(x, link(4, empty))
    False
    >>> has_prefix(x, link(3, link(4, empty)))
    True
    >>> has_prefix(x, link(3, link(3, empty)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2, empty), link(2, link(3, empty)))
    False
    """
    "*** YOUR CODE HERE ***"
    if s == empty and prefix != empty:
        return False
    elif prefix == empty:
        return True
    if first(s) == first(prefix):
        return has_prefix(rest(s), rest(prefix))
    else:
        return False    
            



def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A', empty)))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3, empty)))
    False
    >>> has_sublist(x, link('G', link('T', empty)))
    False
    >>> has_sublist(x, link('A', link('T', link('T', empty))))
    True
    >>> has_sublist(link(1, link(2, link(3, empty))), link(2, empty))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    "*** YOUR CODE HERE ***"
    if s == sublist:
        return True
    if s == empty:
        return False
    if has_prefix(s, sublist):
        return True
    else:
        return has_sublist(rest(s), sublist)    


def has_61A_gene(dna):
    """Returns whether linked list dna contains the CATCAT gene.

    >>> dna = link('C', link('A', link('T', empty)))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_61A_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G', empty)))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_61A_gene(dna)
    True
    >>> has_61A_gene(end)
    False
    """
    "*** YOUR CODE HERE ***"
    gene = link('C', link('A', link('T',link('C', link('A', link('T', empty))))))
    return has_sublist(dna, gene)

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    attempts = []
    def password_protected(amount, this_password):
        nonlocal balance
        nonlocal password
        nonlocal attempts
        if len(attempts) >= 3:
            return "Your account is locked. Attempts: "+ str(attempts)
        if password == this_password:
            if amount <= balance:
                balance -= amount
                return balance
            else:
                return 'Insufficient funds'
        else:
            attempts.append(this_password)       
            return 'Incorrect password'                    
    
    return password_protected    


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    
    typer = withdraw(0, old_password)
    if type(typer) != int:
        return typer
    def j_withdraw(amount, this_pass):
        if this_pass == old_password or this_pass == new_password:
            return withdraw(amount, old_password)
        else:
                   
            return withdraw(amount, this_pass)
           

    return j_withdraw
    

