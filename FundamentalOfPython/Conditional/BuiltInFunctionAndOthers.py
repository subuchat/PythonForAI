import math

def main():
    val = 2.7
    print(round(2.7))
    print("in my overriden round function :",round(val) )

    test_print_builtin()
    my_math_calculation(2, 3)
    my_math_calculation(2, 3,'mul')

    result1 = sum_of_cubes(1, 4)
    result2 = sum_of_cubes(2, 6, 2)

    print(result1, result2)
    

def sum_of_cubes(start, end, step = 1):
    total = 0
    for i in range(start, end, step):
        total += i ** 3
    return total

#Default argument can be set for parameter

def my_math_calculation(a , b , operation = 'add'):
    match(operation):
        case 'add':
            result = a+b
        case 'sub':
            result = a - b
        case 'mul':
            result = a * b
        case 'div':
            result = a / b
        case _:
            result = None
    print("result of my_math_calculation:" , result)


#Test that you can override python provided build-in fucntion
def round(value):
    fraction_part , int_part = math.modf(value)
    if(fraction_part < 0.5):
        return int_part
    else:
        return (int_part+1)
    

def test_print_builtin():
    print("len('Python') : ",len('Python'))
    print("ord('\x06'):", ord('\x06'))
    print("abs(-6):", abs(-6))
    print("round(6.32):", round(6.32))
    print("isinstance(2, int) and isinstance(3.14, float): " , isinstance(2, int) , isinstance(3.14, float))


if __name__ == "__main__":
    main()
