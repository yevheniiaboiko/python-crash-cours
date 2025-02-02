# Write the function body to make the script work without errors.
#
# HINT:
# Use while loop to count sum from 0 to n (included)
def sum_to(n: int) -> int:
    total = 0
    current = 0
    while current <= n:
        total += current
        current += 1
    return total


# Do not change the below's code
if __name__ == "__main__":
    assert sum_to(1) == 1
    assert sum_to(2) == 3
    assert sum_to(3) == 6
    assert sum_to(4) == 10

    n = int(input("Enter a number: "))  
    result = sum_to(n)                 
    print(f"The sum from 0 to {n} is {result}")