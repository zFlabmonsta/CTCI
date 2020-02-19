# String concatentation requires new space to be allocated each time hence O(N^2)
# TO avoid this in python we throw it in to a list and use .join(iterable) to make it O(N)

def compression(string):
    compressed_string_list = []
    compression_count = 0
    last_letter = None
    for l in string:
        if (last_letter == l):
            compression_count += 1
        else:
            compressed_string_list.append(''.join((l, str(compression_count))))
            compression_count = 0
        last_letter = l
    return ''.join(compressed_string_list)

print(compression('aabbaaccdd'))
        

