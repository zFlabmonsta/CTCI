def tree_matching(t1, t2):
    if t1 == None and t2 == None:
        return True
    elif t1 == None or t2 == None:
        return Flase
    else:
        if t1._val == t2._val:
            left_identical = tree_matching(t1._left, t2._left)
            right_identical = tree_matching(t1._right, t2._right)
            return left_identical and right_identical
        return False

def check_subtree(t1, t2):
    if t1 == None:
        return False
    else:
        has_subtree = None
        if (t1._val == t2._val):
            has_subtree = tree_matching(t1, t2)
        if (has_subtree == True):
            return True
        else:
            left = tree_matching(t1._left, t2)
            right = tree_matching(t1._right, t2)
            return left or right

class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

A = Node(10)
B = Node(8)
C = Node(15)
D = Node(7)
E = Node(9)

A._left = B
A._right = C
B._left = D
B._right = E

F = Node(8)
G = Node(7)
H = Node(9)

F._left = G
F._right = H

print(check_subtree(A, F))
