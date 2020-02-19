class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

    def insert_left(self, node):
        self._left = node

    def insert_right(self, node):
        self._right = node

# parse in array in increasing order
def array_to_tree(arr):
    if arr == None:
        return None

    # create root Node
    mid = len(arr)/2
    root = Node(arr[mid])

    i = mid + 1
    curr = root
    while (i < len(arr)):
        curr.insert_right(Node(arr[i]))
        curr = curr._right
        i += 1

    i = mid - 1
    curr = root
    while (i >= 0):
        curr.insert_left(Node(arr[i]))
        curr = curr._left
        i -= 1

    return root

def print_tree(root):
    print(root._val)
    if root._left == None and root._right == None:
        return
    else:
        if root._left != None:
            print_tree(root._left)
        if root._right != None:
            print_tree(root._right)

arr = [1,2,3,4,5,6,7]
root = array_to_tree(arr)
print("printing pre-order traversal")
print_tree(root)

# With the approach above only works if array is sorted
# Another method is to insert it into the correct position but this will be O(NlogN)
# Assuming we also start in the middle
# Another way is to recrusively create new tree starting from the middle, divide and conquer

def array_to_tree_2(arr):
   array_to_tree_2_helper(arr, 0, len(arr) - 1)


def array_to_tree_2_helper(arr, start, end):
    if end >= start:
        return
    else:
        mid = len(arr)/2
        n = Node(arr[mid])
        n.insert_left = array_to_tree_2_helper(arr, 0, mid - 1)
        n.insert_right = array_to_tree_2_helper(arr, mid + 1, len(arr) - 1)
    return n

root = array_to_tree(arr)
print("printing pre-order traversal")
print_tree(root)







