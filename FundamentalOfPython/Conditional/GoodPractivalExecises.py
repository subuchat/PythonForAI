# Check if a traingle is valid.
# A triangle is valid when sum of any 2 side is greater than 3rd side

def is_valid_triangle():
    side1 = float(input("Enter the first side of triangle: "))
    side2 = float(input("Enter the second side of triangle: "))
    side3 = float(input("Enter the third side of triangle: "))

    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")

# Check if a year is leap year or not
def is_leap_year():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Calculate the sum of even numbers from 1 to n
def calculate_even_number_sum():
    n = int(input("Enter a number: "))
    even_sum = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
    '''
    result = 0
    if n >= 2:
        for num in range(2 , n+1 , 2): start , stop , step
            result = num + result
    '''
    print(f"The sum of even numbers from 1 to {n} is: {even_sum}")


def main():
    is_valid_triangle()
    is_leap_year()
    calculate_even_number_sum()

if __name__ == "__main__":
    main()