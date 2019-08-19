def is_unique(word):
    freq_dict = dict()
    for character in word:
        if character in freq_dict:
            return False
        else:
            freq_dict[character] = 1
    return True

print(is_unique("Palindrome"))
print(is_unique("Great Britain"))
print(is_unique(""))