def check_permutation(string1, string2):
    dict1 = dict()
    for character in string1:
        if(character in dict1):
            dict1[character] += 1
        else:
            dict1[character] = 1
    
    if(string2 == ""):
        return False

    for character in string2:
        if(character not in dict1):
            return False
        dict1[character] -= 1
        if(dict1[character] < 0):
            return False
    
    return True
    
print(check_permutation("machine","aminche"))
print(check_permutation("machine","non-machine"))