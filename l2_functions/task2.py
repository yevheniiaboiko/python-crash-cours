
# Declare a function named `join`
# that accepts two strings as parameters
# and returns their concatenation separated
# by whitespace ' '.
#
# For example, call of `join("a", "b")` should return "a b"

def join(str1: str, str2: str) -> str:
    return f"{str1} {str2}"

# Do not change the below's code
if __name__ == "__main__":
    a, b = "Jon", "Doe"

    assert join(a, b) == "Jon Doe"
    assert join(b, a) == "Doe Jon"
    assert join("aba", "baba") == "aba baba"

    print(join(a, b)) 
    print(join(b, a))  
    print(join("aba", "baba"))