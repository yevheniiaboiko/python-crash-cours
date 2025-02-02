from typing import Iterable


# Finish the function to make the script work without errors.
#
# NOTE:
# Iterable is any object that can be converted into an iterator.
# You're already familiar with `list`, `str` which are Iterables
def reverse(c: Iterable) -> Iterable:
    if isinstance(c, str):
        return c[::-1]
    elif isinstance(c, tuple):
        return tuple(reversed(c))
    else:
        return list(reversed(c))


# Do not change the below's code
if __name__ == "__main__":
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse("abc") == "cba"

    # NOTE:
    # Here we used a new type to you called tuple.
    # Tuple is an immutable collection of values defined inside parentheses,
    # as you see below. Often, we can omit the parentheses and write something
    # like this
    #
    # x = 3, 5, 6
    #
    # which is equivalent to
    #
    # x = (3, 5, 6)
    assert reverse((3, 4, 5)) == (5, 4, 3)

    user_input = input("Enter a list, string, or tuple to reverse: ")
    try:
        user_data = eval(user_input)
        result = reverse(user_data)
        print("Reversed:", result)
    except:
        print("Invalid input. Please enter a valid list, string, or tuple.")