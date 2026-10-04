# Exercise 1
def is_valid_email(text):
    if "@" in text and "." in text:
        return "Valid"
    else:
        return "Invalid"

# Exercise 2
def remove_vowels(text):
    b = ""
    for c in text:
        if c not in "aeiouAEIOU":
            b += c
    return b

# Exercise 3
def get_initials(text):
    b = ""
    for x in text.split():
        b += x[0].upper() + "."
    return b

# Exercise 4
def extract_year(text):
    b = text.split()
    c = "False"

    for d in b:
        e = ""
        for f in d:
            if f.isdigit():
                e += f

        if len(e) == 4 and c == "False":
            c = e

    return c

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
