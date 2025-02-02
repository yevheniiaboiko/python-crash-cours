# Write a function that returns True if
# string `s` contain vowels (A, E, I, O, U, a, e, i, o, u)
# and False otherwise
def contains_vowels(s: str) -> bool:
    return any(char in "AEIOUaeiou" for char in s)


# Do not change the below's code
if __name__ == "__main__":
    assert contains_vowels("aghfn") is True
    assert contains_vowels("bnv") is False
    assert contains_vowels("AER") is True
    assert contains_vowels("LKU") is True
