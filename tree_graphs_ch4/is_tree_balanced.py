class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None


def tree_height(root):
    if root is None:
        return 0
    elif root._left is None and root._right is None:
        return 1
    else:
        left_height = tree_height(root._left)
        right_height = tree_height(root._right)
        return 1 + max(left_height, right_height)

def is_balanced(root):
    if root == None:
        return True
    left_height = tree_height(root._left)
    right_height = tree_height(root._right)

    height_diff = abs(left_height - right_height)
    return height_diff <= 1

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A._left = B
A._right = C
B._left = D
B._right = E
D._left = F
print(is_balanced(A))

A._left = None
A._right = None
B._left = None
B._left = None
C._right = None
C._right = None
D._right = None
D._right = None
E._right = None
E._right = None
F._right = None
F._right = None

A._left = B
A._right = C
B._left = D
B._right = E
C._left = F
print(is_balanced(A))
