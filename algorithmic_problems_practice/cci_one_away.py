def one_away(string1,string2):
    idx = 0

    if(len(string1) > len(string2)):
        aux = string1
        string2 = string1
        string1 = aux

    if(len(string2) -len(string1) > 1):
        return False    

    while(idx < len(string1) and idx < len(string2)):
        char1 = string1[idx]
        char2 = string2[idx]
        
        if(char1 == char2):
            idx += 1
        else:
            if(idx == len(string1)-1 and idx == len(string2)-1):
                return True
            elif(idx == len(string1)-1 and idx == len(string2) - 2):
                return char1 == string2[idx+1]
            elif(string1[idx+1] == char2):
                return string1[idx+1:] == string2[idx:]
            elif(char1 == string2[idx+1]):
                return string1[idx:] == string2[idx+1:] 
            elif(string1[idx+1] == string2[idx+1]):
                return string1[idx+1:] == string2[idx+1:] 
            else:
                return False
    return True

print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))