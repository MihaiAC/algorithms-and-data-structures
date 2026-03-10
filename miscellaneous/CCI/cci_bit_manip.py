def get_bit(number,position):
    mask = 1 << position
    if(mask & number == 0):
        return 0
    return 1

def set_bit(number,position):
    mask = 1 << position
    number = number | mask
    return number

def clear_bit(number,position):
    mask = ~(1 << position)
    return number & mask

def insertion(nn,mm,ii,jj):
    for k in range(jj-ii+1):
        mbit = mm & 1
        mm = mm >> 1
        pos = ii + k
        if(mbit != 0):
            nn = set_bit(nn,pos)
        else:
            nn = clear_bit(nn,pos)
    return nn

def bin_to_string(number):
    if(number <= 0 or number >= 1):
        print("Error")
        return 0
    
    bin_string = ['0','.']
    for ii in range(32):
        number = number * 2
        if(number >= 1):
            bin_string.append('1')
            number = number - 1
        else:
            bin_string.append('0')
        if(number == 0):
            print("".join(bin_string))
            return 0
    
    print("Error")
    return 0

bin_to_string(0.25)
bin_to_string(0.33)
bin_to_string(0.375)