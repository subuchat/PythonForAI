
def main():
    n = int(input("Enter a number to calculate its factorial: "))
    result = factorial(n)
    if result is not None:
        print(f"The factorial of {n} is {result}.") 
    else:
        print("Factorial calculation was not performed due to invalid input.")

    #Only 3 out of 5 singers can perform in a concert. Write a program to find the number of ways in w hich the singers can be selected.
    #P(5,3) = 5! / (5-3)! = 5! / 2! = 60
    ways = int(factorial(5) / factorial(5 - 3))
    print(f"The number of ways to select 3 singers from 5 is {ways}.")

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    elif n == 0 or n == 1:
        return 1
    else:
        '''
        result = 1
        for i in range(2, n + 1):
            result *= i
        print(f"The factorial of {n} is {result}.")
        
        '''
        return n * factorial(n - 1)

if __name__ == "__main__":
    main()