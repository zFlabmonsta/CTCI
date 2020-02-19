# We need to understand that if a string is rotated
# There will be two points of that string where 
# one side is the left, and right 
# i.e. waterbottle --> erbottlewat
# left side: x = wat, right side: y = erbottle
# That means, the original word is xy --> yx
# therefore if we repeat yxyx, xy is contained in yxyx,

def rotation_substring(s1, s2):
    if (len(s1) != len(s2)):
        return False
    s = str(s1) + (s1)
    return s2 in s



