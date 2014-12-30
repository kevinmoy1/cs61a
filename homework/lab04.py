def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

# Q6
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"
    total = 0
    if len(lst) == 0:
        return 0
    for x in lst : 
        if type(x) == list:
            total += deep_len(x)
        else:
            total += 1
    return total
    
# Q7
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    totlst = []
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    if lst1[0] >= lst2[0]:
        totlst.append(lst2[0])
        lst2.remove(lst2[0])
    else:
        totlst.append(lst1[0])
        lst1.remove(lst1[0])
    
    return totlst+merge(lst1,lst2)
        
        
    
            

# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    totlist = []
    for x in seq:
        if fn(x) <= upper and fn(x) >= lower:
            lst = [x,fn(x)]
            totlist.append(lst)
    return totlist

# Q13
def deck():
    "*** YOUR CODE HERE ***"
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
    number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = []
    for x in suits:
        for y in number:
            card = [x,y]
            deck.append(card)
    return deck
    

def sort_deck(deck):
    "*** YOUR CODE HERE ***"
    sorted_list = []
    lsth = []
    lstd = []
    lsts = []
    lstc = []
    for x in deck:
        if x[0] == "Hearts":
            lsth.append(x[1])
        if x[0] == "Diamonds":
            lstd.append(x[1])
        if x[0] == "Spades":
            lsts.append(x[1])
        if x[0] == "Clubs":
            lstc.append(x[1])
    tot += [lsth, lstd, lstc, lsts]
    
    
