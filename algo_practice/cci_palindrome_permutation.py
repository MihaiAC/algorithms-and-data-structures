def set_bits_count(bin_number):
    count = 0
    while(bin_number):
        bin_number &= bin_number - 1
        count += 1
    return count


def palindrome_permutation(string1):
    string1 = string1.lower()
    string1 = "".join(string1.split(" "))
    bin_counts = 0

    for character in string1:
        offset = ord(character) - ord('a')
        mask = 1 << offset
        bin_counts = bin_counts ^ mask
    
    nr_set_bits = set_bits_count(bin_counts)
    if(nr_set_bits == 0 or nr_set_bits == 1):
        return True
    return False

print(palindrome_permutation('Tact Coa'))
print(palindrome_permutation("not a palindrome"))
print(palindrome_permutation(" "))