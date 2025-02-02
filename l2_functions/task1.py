from typing import Union
Number = Union [int | float | complex]


# Write the body of the function to make the script
# work without errors
def sqr(n: Number) -> Number:
    return n*n 


if __name__ == "__main__":

    user_input = input("Enter a number (int, float, or complex): ")
    
    try:
        if 'j' in user_input:
            number = complex(user_input)
        elif '.' in user_input:
            number = float(user_input)
        else:
            number = int(user_input)
        
        result = sqr(number)
        print(f"The square of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    # Do not change the below asserts
    assert sqr(2) == 4
    assert sqr(4.0) == 16
    assert sqr(3 + 2j) == 5 + 12j

    