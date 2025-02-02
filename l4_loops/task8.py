# Use `for` loop to calculate the amount
# of positive number in a list of integers `n`
def count_positive(n: list[int]) -> int:
    count = 0
    for num in n:
        if num > 0:  
            count += 1  
    return count


# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4

    n = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    result = count_positive(n) 
    
    print(f"The number of positive numbers is: {result}")
