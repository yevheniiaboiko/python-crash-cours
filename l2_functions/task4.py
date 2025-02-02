# Declare and write the body of the function named `my_len`.
# This function should accept an Iterable as a parameter
# and return its length

from typing import Iterable 

def my_len(c: Iterable) -> int:
    length = 0
    for _ in c:
        length +=1
    return length

# Do not change the below's code
if __name__ == "__main__":
    assert my_len([3, 4, 5]) == 3
    assert my_len("abv") == 3
    assert my_len({"a": 1, "b": 3}) == 2
    assert my_len((3, 4, 5)) == 3

    user_input = input("Enter an iterable(e.g., list, string, tuple, dictionare): ")

    try:
        iterable = eval(user_input)
        if isinstance(iterable, Iterable):
            print(f"The length of the given iterable is: {my_len(iterable)}")
        else:
            print("The provided input is not an iterable.")
    except:
        print("Invalid input. Please provide a valid iterable.")
