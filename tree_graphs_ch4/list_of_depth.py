class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

class LinkNode:
    def __init__(self, val):
        self._next = None
        self._val = val

def list_of_depths(root):
    queue = []
    depth_list = []
    if root is None:
        return

    current_level = 1
    items_left = 1
    queue.append(root)
    while (queue):
        depth_list.append(create_link_list(queue))
        add_next_level(queue)

    return depth_list
        

def add_next_level(list):
    i = 0
    length = len(list)
    while (i < length):
        item = list.pop(0)
        if (item._left != None):
            list.append(item._left)
        if (item._right != None):
            list.append(item._right)
        i += 1

def print_depth_list(list):
    i = 1
    for lnk in list:
        print("printing level" + str(i))
        curr = lnk
        while (curr != None):
            print(curr._val)
            curr = curr._next
        i += 1

def create_link_list(list):
    head = LinkNode(list[0]._val)
    i = 1
    curr = head
    while (i < len(list)):
        curr._next = LinkNode(list[i]._val)
        curr = curr._next
        i += 1

    return head

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A._left = B
A._right = C
C._right = D

l = list_of_depths(A)
print_depth_list(l)

