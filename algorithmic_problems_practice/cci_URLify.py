def URLify(string1):
    return "%20".join(string1.split(" "))

print(URLify("Mr John Smith"))