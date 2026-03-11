import sys


def solution(sol_input):
    # nrmult_right[ii]=n <=> there are n multiples of l[ii] in l[ii+1:]
    nrmult_right = []
    nr_passcodes = 0
    for _ in range(len(sol_input)):
        nrmult_right.append(0)

    for ii in range(len(sol_input) - 2, -1, -1):
        for jj in range(ii + 1, len(sol_input)):
            if sol_input[ii] > sol_input[jj]:
                continue
            elif sol_input[jj] % sol_input[ii] == 0:
                nrmult_right[ii] += 1
                nr_passcodes += nrmult_right[jj]
    return nr_passcodes


ls = []
for ii in sys.argv[1:]:
    ls.append(int(ii))
print(solution(ls))
