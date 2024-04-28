""" Homework 07: Special Method, Linked Lists and Mutable Trees"""


#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """

    def __init__(self, lst):
        self.lst = lst
        while len(self.lst) > 1 and self.lst[-1] == 0:
            self.lst.pop()

    def __repr__(self):
        return f'Polynomial({self.lst})'

    def __str__(self):
        ans = f'{self.lst[0]}'
        for i in range(1, len(self.lst)):
            ans += f' + {self.lst[i]}*x^{i}'
        return ans

    def __add__(self, other):
        newline = []
        min_lst = self.lst if len(self.lst) <= len(other.lst) else other.lst
        max_lst = self.lst if len(self.lst) > len(other.lst) else other.lst
        for i in range(len(min_lst)):
            newline += [self.lst[i] + other.lst[i]]
        newline += max_lst[len(min_lst):]
        return Polynomial(newline)

    def __mul__(self, other):
        newline = []
        min_lst = self.lst if len(self.lst) <= len(other.lst) else other.lst
        max_lst = self.lst if len(self.lst) > len(other.lst) else other.lst
        for y in range(len(max_lst) + len(min_lst)):
            newline.append(0)
        for index in range(len(min_lst) + len(max_lst) - 1):
            for x in range(index + 1):
                if 0 <= index - x < len(max_lst) and x < len(min_lst):
                    newline[index] += min_lst[x] * max_lst[index - x]
        return Polynomial(newline)


def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    store_num = []
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        if isinstance(lnk.first, Link):
            remove_duplicates(lnk.first)
        else:
            store_num.append(lnk.first)
            if lnk.rest.first in store_num:
                lnk.rest = lnk.rest.rest  # 清理掉
            else:
                lnk = lnk.rest  # 指针指向下个节点


def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    if lnk is Link.empty:
        return lnk
    if lnk.rest is Link.empty:
        return lnk
    former = Link.empty    # 保留first，防止丢失
    curr = lnk
    follow = lnk.rest      # 保留rest，防止丢失
    while curr is not Link.empty:
        curr.rest = former
        former = curr
        curr = follow
        if follow is not Link.empty:
            follow = follow.rest
    result = former
    return result


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()

    def __eq__(self, other):  # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        if self.label != other.label or len(self.branches) != len(other.branches):
            return False
        else:
            for index in range(len(self.branches)):
                if not self.branches[index] == other.branches[index]:  # 递归调用
                    return False
            return True


def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if t.label == value:
        yield [value]
    for b in t.branches:
        for path in generate_paths(b, value):   # 递归，重点是：该函数是什么，返回什么
            yield [t.label] + path


def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    if total == 0:                                # 照着上面写，没啥好说的
        return Tree('1')
    if total < 0 or len(denominations) == 0:
        return None
    result = Tree(f'{total}, {denominations}')
    t1 = count_coins_tree(total - denominations[0], denominations)
    t2 = count_coins_tree(total, denominations[1:])
    if t2:
        without_current = t2
    else:
        without_current = None
    if t1:
        with_current = t1
    else:
        with_current = None
    if with_current and without_current:
        result.branches = [without_current] + [with_current]
    elif with_current:
        result.branches = [with_current]
    elif without_current:
        result.branches = [without_current]
    else:
        result = None
    return result


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """

    def bst_min(t):
        if t.is_leaf():
            return t.label
        return min(t.label, bst_min(t.branches[0]))      # 返回t中最小label

    def bst_max(t):
        if t.is_leaf():
            return t.label
        return max(t.label, bst_max(t.branches[-1]))      # 返回t中最大label

    if t.is_leaf():
        return True
    if len(t.branches) == 1:
        b = t.branches[0]
        if not is_bst(b):                                     # 若该树是合法的，那么其子树必须合法
            return False
        return bst_max(b) <= t.label or bst_min(b) > t.label  # 子树满足任一
    elif len(t.branches) == 2:
        b1, b2 = t.branches[0], t.branches[1]
        if not (is_bst(b1) and is_bst(b2)):                   # 左子树的最大label小于root且右子树的最小label大于等于root
            return False
        return bst_max(b1) <= t.label < bst_min(b2)
    else:
        return False


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    fast, slow = lnk, lnk
    while fast is not Link.empty and fast.rest is not Link.empty:
        fast = fast.rest.rest
        slow = slow.rest
        if slow is fast:
            return True
    return False


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    for b in t.branches:
        balance_tree(b)
    max_total = max([b.total for b in t.branches], default=0)  # 默认值0，防止列表空报错
    for b in t.branches:
        b.label += max_total - b.total
    t.total = t.label + max_total * len(t.branches)


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
