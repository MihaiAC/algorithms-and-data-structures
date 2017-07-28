import re

#Laboratory 1 Inf2A
p11 = "[0-9][0-9][0-9].*"
p12 = "[a-zA-Z]+ly"
p13 = "(wh|Wh)[a-zA-Z]*"

#Tutorial 2 Inf2A
pt1b = "(([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))([Ee][+-]?[0-9]+)?"

def exercise12(s):
    for i in s:
        l = re.findall(p13,i)
        if(len(l) == 0):
            print("* " + i[0:2] + " " + i)
        else:
            print("- " + i[0:2] + " " + i)

def exercise14(list, prefix):
    l = len(prefix)
    for i in list:
        if(i[0:l] == prefix):
            print("* " + i)
        else:
            print(i)

if __name__ == '__main__':
    s = "1.35E-2"
    print(re.findall(pt1b,s))
