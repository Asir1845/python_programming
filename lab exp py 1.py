def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)   
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
number = int(input("Enter an integer: "))
if number % 2 != 0:
    print("the given is an odd number")
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")
else:
    print("the given number is even")
    if is_palindrome(number):
        print(f"The number {number} is a palindrome.")
    else:
        print(f"The number {number} is not a palindrome.")s
