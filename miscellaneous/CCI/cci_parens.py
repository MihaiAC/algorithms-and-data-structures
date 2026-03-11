def cci_parens(n):
    ls = [["(", 1, 0]]

    while True:
        if len(ls) == 0:
            break

        new_ls = []

        for elem in ls:
            left = elem[1]
            right = elem[2]
            comb = elem[0]
            if left == n:
                print(comb + (")" * (left - right)))
                continue

            if right < left:
                new_ls.append([comb + ")", left, right + 1])
            new_ls.append([comb + "(", left + 1, right])

        del ls
        ls = new_ls


cci_parens(3)
