# Write the body of the function to make the script work without errors
def is_vowel(c: str) -> bool:
    return c.lower() in "aeiou"

if __name__ == "__main__":
    # Do not change the below asserts
    assert is_vowel("a") is True
    assert is_vowel("e") is True
    assert is_vowel("z") is False
    assert is_vowel("B") is False

    char = input("Enter a character: ")
    print(f"Is '{char}' a vowel? {is_vowel(char)}")