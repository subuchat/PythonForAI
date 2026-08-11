from unittest import result


def main():
    #print("This will calculate the area of a triangle")
    #areaofTriangle()
    #findaExpression()
    #changeTemperatureUnittoFahrenheit()
    #checkSalary()
    #calculateSimpleInterest()
    #swapVariablesValues()
    checkBooleanExpression()
    

def areaofTriangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

def findaExpression():
    # Taking input from console
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))

    output = (x**y + (x+y)**(x-y) )
    # Print the output
    print(output)

def changeTemperatureUnittoFahrenheit():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")

def checkSalary():
    '''
    You are given a base salary and a bonus amount. Update the salary by adding the bonus using an assignment operator. 
    Then, check if the updated salary is more than 50000 and the bonus is more than 5000.
    '''
    # Taking input
    salary = int(input())
    bonus = int(input())

    salary += bonus
    eligible = ((salary > 50000) and (bonus > 5000))
    # Print the output
    print(eligible)

def calculateSimpleInterest():
    '''
    You are given a principal amount, rate of interest, and time in years. Calculate the simple interest using the formula: 
    Simple Interest = (Principal * Rate * Time) / 100. 
    Then, check if the simple interest is greater than 1000 and the principal amount is greater than 5000.
    '''
    # Taking input
    principal = float(input("Provide the principal amount: "))
    rate = float(input("Provide the rate of interest: "))
    time = float(input("Provide the time in years: "))

    simple_interest = (principal * rate * time) / 100
    print(simple_interest)

def swapVariablesValues():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: ")) 

    # Swapping values using a temporary variable
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")

def checkBooleanExpression():
    # Taking input
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    # Write your code here
    result = bool((a and not b) or (b and not c) ) # tricky , check removing bool caste for o o o input, it will return 0 instead of False

    # Print the output
    print(result)



if __name__ == "__main__":
    main()
