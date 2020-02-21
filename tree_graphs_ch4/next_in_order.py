class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

# Could use a stack but that is O(N)

# Case 1: If right node has a right subtree,
# then the next node would be the most left of 
# the right subtree

# Case 2: if the node element is less than the root,
# You shift the pointers, until point matches the Node

def find_successor(root, val):
    def find_current (root, val):
        curr = root
        while (curr != None):
            if val < curr._val:
                curr = curr._left
            elif val > curr._val:
                curr = curr._right
            else:
                return curr
        return curr
    
    curr = find_current(root, val)
    if curr == None:
        return None

    def most_left(root):
        curr = root
        while (curr._left != None):
            curr = curr._left
        return curr

    if curr._right != None:
        return most_left(root)

    predecessor = root
    successor = None
    while (curr._val != predecessor._val):
        if (curr._val < predecessor._val):
            successor = predecessor
            predecessor = predecessor._left
        else:
            predecessor = predecessor._right

    return successor._val


A = Node(11)
B = Node(20)
C = Node(5)

B._left = C
B._right = 20

print(find_successor(B, 5))
