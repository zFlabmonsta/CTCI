class Node:
    def __init__(self, val, n=None):
        self._val = val
        self._next = n

def remove_dup(link_list):
    head = link_list
    # iteratre through and add to dict
    dic = {}
    curr = head
    while (curr != None):
        if curr._val not in dic:
            dic[curr._val] = 1
        else:
            dic[curr._val] += 1
        curr = curr._next

    curr = head
    while (curr._next != None):
        if dic[curr._val] > 1:
            tmp = curr
            curr = curr._next
            tmp._next = None
        else:
            curr = curr._next
    return link_list

def print_list(linked_list):
    curr = linked_list
    while (curr != None):
        print(curr._val)
        curr = curr._next
    print("")


# Tests
l1 = remove_dup(Node(1, Node(2, Node(3))))
l2 = remove_dup(Node(1, Node(1)))
l3 = remove_dup(Node(1, Node(3, Node(8, Node(3)))))

print_list(l1)
print_list(l2)
print_list(l3)



