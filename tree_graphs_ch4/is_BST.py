class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

INF = 1000000

def is_bst(root):
    if root == None:
        return True
    return helper_bst(root, -INF, root._val, root._val, INF)

def helper_bst(root, left_lower, left_upper, right_lower, right_upper):
    if root == None:
        return True
    if root._left == None and root._right == None:
        return True
    else:
        left_bst = helper_bst(root._left, left_lower, root._left._val, root._left._val, left_upper)
        right_bst = helper_bst(root._right, right_lower, root._right._val, root._right._val, right_upper)
        
        if root._left._val > root._val or root._left._val < left_lower:
           return False
        if root._right._val < root._val or root._right._val >= right_upper:
           return False

        return left_bst and right_bst

A = Node(10)
B = Node(7)
C = Node(15)
D = Node(3)
E = Node(15)
F = Node(11)
G = Node(17)

A._left = B
A._right = C
B._left = D
B._right = E
C._left = F
C._right = E

print(is_bst(A))



