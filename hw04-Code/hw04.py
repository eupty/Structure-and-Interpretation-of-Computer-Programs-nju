""" Homework 4: Data Abstraction and Trees"""

from math import sqrt
from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    ans = []
    i = 0
    while i < len(lst1):
        ans += [[lst1[i]] + [lst2[i]]]
        i += 1
    return ans
        


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt((get_lat(city1) - get_lat(city2))**2 + (get_lon(city1) - get_lon(city2))**2)


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    city0 = make_city('0', lat, lon)
    if distance(city0, city1) < distance(city0, city2):
        return get_name(city1)
    else:
        return get_name(city2)


def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    if label(t) == 'nut':
        return True
    elif label(t) != 'nut' and is_leaf(t):
        return False
    else:
        for b in branches(t):
            if nut_finder(b):
                return True
        return False

def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    ans = []
    ans1 = []
    if is_leaf(t):
        for c in values:
            ans += [tree(c)]
        return tree(label(t), ans)
    else:
        for b in branches(t):
            ans1 += [sprout_leaves(b, values)]
        return tree(label(t), ans1)


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    ans = []
    i = 0
    label0 = label(t1) + label(t2)
    if is_leaf(t1) or is_leaf(t2):
        return tree(label0, branches(t1) + branches(t2))
    for b in range(min(len(branches(t1)), len(branches(t2)))):
        ans += [add_trees(branches(t1)[b], branches(t2)[b])]
    if len(branches(t1)) > len(branches(t2)):
        for c in range(len(branches(t2)), len(branches(t1))):
            ans += [branches(t1)[c]]
    if len(branches(t2)) > len(branches(t1)):
        for d in range(len(branches(t1)), len(branches(t2))):
            ans += [branches(t2)[d]]
    return tree(label0, ans)


def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    ans = 0
    if is_leaf(t) and label(t) >= n:
        return 1
    elif is_leaf(t):
        return 0
    elif label(t) >= n:
        ans1 = 1
        for c in branches(t):
            ans1 += bigpath(c, 0)
        return ans1
    else:
        for b in branches(t):
            if isNum(t):
                ans += bigpath(b, n - label(t))
            else:
                ans += bigpath(b, n)
        return ans



def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """

    def helper(t, n, index):
        ans = 0
        if is_leaf(t) and label(t) >= n:
            return 1
        elif is_leaf(t):
            return 0
        elif label(t) >= n and not is_leaf(t):
            ans1 = 1
            for c in branches(t):
                if label(t) >= 0 and index == 1:
                    ans1 += helper(c, n, 1) + helper(c, n - label(t), 0)
                elif label(t) >= 0 and index == 0:
                    ans1 += helper(c, n - label(t), 0)
                else:
                    ans1 += helper(c, n, 0) + helper(c, n, 1)
            return ans1
        else:
            for b in branches(t):
                if label(t) >= 0 and index == 1:
                    ans += helper(b, n, 1) + helper(b, n - label(t), 0)
                elif label(t) >= 0 and index == 0:
                    ans += helper(b, n - label(t), 0)
                else:
                    ans += helper(b, n, 0) + helper(b, n, 1)
            return ans
    return helper(t, n, 1)

##########################
# Just for fun Questions #
##########################


def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"


def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')
