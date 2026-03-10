def cci_parens(n):
    ls = [['(',1,0]]

    while(True):
        if(len(ls) == 0):
            break
        
        new_ls = []

        for elem in ls:
            l = elem[1]
            r = elem[2]
            comb = elem[0]
            if(l == n):
                print(comb + (')'*(l-r)))
                continue
            
            if(r < l):
                new_ls.append([comb+')',l,r+1])
            new_ls.append([comb+'(',l+1,r])
        
        del ls
        ls = new_ls

cci_parens(3)