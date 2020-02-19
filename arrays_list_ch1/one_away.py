def one_away(s1, s2):
    def str_parser_dict(s):
        dict = {}
        for letter in s:
            if (letter not in dict):
                dict[letter] = 1
            else:
                dict[letter] += 1
        return dict

    def str_cmp_dict(dic, s):
        for letter in s:
            if letter in dic:
                dic[letter] -= 1
        return dic

    dic = str_parser_dict(s1)
    dic = str_cmp_dict(dic, s2)

    edited = 0
    for v in dic.values():
        if v >= 1:
            edited += v
    return edited <= 1

print(one_away("a", "g"))
print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("eee", "aaa"))
print(one_away("ebe", "aba"))
