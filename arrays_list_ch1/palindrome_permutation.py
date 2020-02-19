# Brute Force Method
def permutation(string):
    list = []
    help_permutation("", string, list)
    return list

def help_permutation(perm, available_string, perm_list):
    if not available_string:
        perm_list.append(perm)
        return
    else:
        i = 0
        while (i < len(available_string)):
            perm += available_string[i]
            new_available_string = available_string[:i] + available_string[i+1:]
            help_permutation(perm, new_available_string, perm_list)
            perm = perm[:-1]
            i += 1

def is_palindrome(string):
    last = len(string) - 1
    first = 0

    while (first < last):
        if (string[first] != string[last]):
            return False
        first += 1
        last -= 1

    return True

def permutation_contains_palindrome(string):
    list_perms = permutation(string)
    for perm in list_perms:
        if is_palindrome(perm):
            return True
    return False

print(permutation_contains_palindrome("abcdabcd"))
print(permutation_contains_palindrome("zzasnnn"))

# If understand the features of palindrome, it can easily by optimised with a hashtable
# features: all even, one or zero odd characters

def permutation_contains_palindrome_2(string):
    count_chars = {}
    for c in string:
        if (c not in count_chars):
            count_chars[c] = 1
        else:
            count_chars[c] += 1
   
    odd_count = 0
    for val in count_chars.values():
        if (val % 2 != 0):
            odd_count += 1

    return odd_count <= 1

print(permutation_contains_palindrome_2("abcdabcd"))
print(permutation_contains_palindrome_2("zzasnnn"))





