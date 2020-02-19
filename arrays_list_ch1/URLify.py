def urlify(url, end):
    new_url = ""
    for l in range(0, end):
        if url[l] == " ":
            new_url = new_url + "%20"
        else:
            new_url = new_url + url[l]
    return new_url

assert(urlify("hello world  ", 11) == "hello%20world")
assert(urlify("hello world bob    ", 15) == "hello%20world%20bob")

# Tricky this will not be O(N) because string in python are immutable
# every time we are appending a string to the end of url, what is actually
# happening in memory is a new space get allocated and the string is slotted IndentationError
# new space, making it O(N^2)

def urlify1(url, end):
    # because strings are immutable we turn it into a list O(N)
    list = str_to_list(url)

    i = end - 1
    tail = len(url) - 1
    while i >= 0:
        if (list[i] == ' '):
            list[tail] = '0'
            list[tail - 1] = '2'
            list[tail - 2] = '%'
            tail -= 3
        else:
            list[tail] = list[i]
            tail -= 1 
        i -= 1
    # O(N) method of python turning list into string
    return ''.join(list)

def str_to_list(str):
    list = []
    for c in str:
        list.append(c)
    return list

a = "hello world  " 
b = "hello world bob    "
assert(urlify1(a, 11) == "hello%20world")
assert(urlify1(b, 15) == "hello%20world%20bob")


