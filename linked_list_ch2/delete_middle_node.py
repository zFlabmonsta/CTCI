class Node:
    def __init__(self, val, n):
        self._val = val
        self._next = n

def delete_middle_node(lnk_list):
    if (lnk_list == None):
        return
    list_length = 0
    curr = lnk_list
    while (curr != None):
        

