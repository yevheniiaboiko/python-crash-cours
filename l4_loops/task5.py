# Use `for` loop to check if character `c` is present in
# string `s`.
#
# Return `True` is character is present. Return `False` otherwise
def has_char(s: str, c: str) -> bool:
    return c in s


# Do not change the below's code
if __name__ == "__main__":
    assert has_char("lfhyt", "f") == True
    assert has_char("abbaabba", "c") == False


    s = input("Enter a string: ")  # Take string input
    c = input("Enter a character to search for: ")  # Take character input
    
    result = has_char(s, c)  # Call the has_char function
    
    print(f"Is the character '{c}' present in the string '{s}'? {result}")