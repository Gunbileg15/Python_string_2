# Exercise 1
def is_valid_email(text):
    if "@" in text and "." in text:
        return "Valid"
    else:
        return "Invalid"
        pass

# Exercise 2
def remove_vowels(text):
    b = ""
    for c in text:
        if c not in "aeiouAEIOU":
            b += c
    return c
    pass

# Exercise 3
def get_initials(text):
    b = ""
    for x in text.split():
        b += x[0].upper() + "."
    return b
    pass

# Exercise 4
def extract_year(text):
    for word in text.split():
        e = ""
        for char in word:
            if char.isdigit():
                e += char
        if len(e) == 4:
            return e
        else:
            return False
    pass

# Exercise 5
def is_palindrome(text):
    b = ""
    for x in text:
        if x.isalnum():
            b += x.lower()

    if b == b[::-1]:
        return "true"
    else:
        return "false"
    pass
