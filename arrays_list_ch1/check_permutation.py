def check_permutation(x, y):
    x = sorted(x)
    y = sorted(y)

    if (len(x) != len(y)):
        return False

    for i in range(0, len(x)):
        if x[i] != y[i]:
            return False
    return True

assert(check_permutation("", "") == True)
assert(check_permutation("abc", "cba") == True)
assert(check_permutation("abc", "def") == False)
assert(check_permutation("abcd", "abc") == False)

# Because T(N) = O(NlogN) + 2 * O(N), its is O(NlogN)

# We can improve this by using hash tables or dictionary and count/check the frequency of each letter
# to make it O(N)

def check_permutation1(x, y):
    freq = {}
    for letter in x:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    for letter in y:
        if letter in freq:
            freq[letter] -= 1
        else:
            freq[letter] = 1

    for k in freq.values():
        if not k == 0:
            return False

    return True

assert(check_permutation1("", "") == True)
assert(check_permutation1("abc", "cba") == True)
assert(check_permutation1("abc", "def") == False)
assert(check_permutation1("abcd", "abc") == False)
