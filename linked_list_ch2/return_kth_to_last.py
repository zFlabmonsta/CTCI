class Node:
    def __init__(self, val, n=None):
        self._val = val
        self._next = n

def kth_to_last(lnk_list, kth):
    if lnk_list == None:
        return

    if (kth == 1):
        tmp = lnk_list
        lnk_list = lnk_list._next
        tmp._next = None
    else:
        tmp = None

    curr = lnk_list
    prev = None
    curr_pos = 1
    while (curr != None):
        if (curr_pos == kth and kth != 1):
           tmp = curr
           prev._next = curr._next
           curr._next = None
           curr = prev._next
        else:
            prev = curr
            curr = curr._next
        curr_pos += 1

    prev._next = tmp

head = Node(1, Node(2, Node(3, Node(4))))
kth_to_last(head, 1)

