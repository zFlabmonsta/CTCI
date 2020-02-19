# Naive method O(n^2)
def isUnique_1(word):
    for i in range (0, len(word)):
        for j in range (i + 1, len(word)):
            if (word[i] == word[j]):
                return False
    return True

assert(isUnique_1("") == True)
assert(isUnique_1("a") == True)
assert(isUnique_1("aa") == False)
assert(isUnique_1("abc") == True)
assert(isUnique_1("abbc") == False)

# Faster method O(n), using dictionary 
def isUnique_2(word):
    d = {}
    for char in word:
        if char in d:
            return False
        else:
            d[char] = 1
    return True

assert(isUnique_2("") == True)
assert(isUnique_2 ("a") == True)
assert(isUnique_2("aa") == False)
assert(isUnique_2("abc") == True)
assert(isUnique_2("abbc") == False)

# it is not possible to improve the time of the algorithm without using additional data structure
