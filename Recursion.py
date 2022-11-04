# Recursion

# cycles can make ur program function faster,
# recursion makes programer function faster,
# choose what's more important to you

# recursion functions are made from 2 parts - base part/exception part

def factorial(n):  # Finding a factiorial of a given number
    if n == 1:  # exception
        return 1
    return n * factorial(n - 1)  # base


"""print(f"factorial of 5 ={factorial(5)}")
print(f"factorial of 7 ={factorial(7)}")
print(f"factorial of 14 ={factorial(14)}")
print(f"It is {factorial(int(input('What factorial do you want to count?: ')))}")

"""

print(factorial(4))
