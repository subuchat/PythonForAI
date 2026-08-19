import builtins
import math

def main():
    val = 2.7
    print(builtins.round(val))
    print("in my overriden round function :",round(val) )

    test_print_builtin()
    my_math_calculation(2, 3)
    my_math_calculation(2, 3,'mul')

    result1 = sum_of_cubes(1, 4)
    result2 = sum_of_cubes(2, 6, 2)

    print(result1, result2)

    nested_function_example()
    #If we return inner function itself , instead of calling it - outside function data is remembered.
    first_val = 50
    function_add = addition_trick_function(first_val) # Another type of nested function.
    print("Function type prints : ",type(function_add))
    add_result = function_add(30) # 50 remembered in value variable in last call
    print("Addition result: ", add_result)

    #recursion function
    fact_res = factorial(5)
    print("Factorial(5): ",fact_res)

    #iterative vs Recursive
    sum = iterative_sum(5)
    print("Sum till int 5: ", sum)
    sum = recursive_sum(5)
    print("Recursive way sum till val 5: ", sum)

    # Function can return multiple value , also unused value can be kept in _ placeholder

    sum , mul , div,_ = calculate( 4, 5)
    print(f"Sum: {sum} Multiplicatoin: {mul} Division: {div}")

    a, b = string_properties('upGrad')
    print("a:",a)
    print("b:",b)

    #End of main

def string_properties(my_str):
    n_vowels = 0
    for ch in my_str:
        if ch in 'AEIOUaeiou':
            n_vowels += 1

    return n_vowels, len(my_str)


def calculate(x,y):
    return x+y , x * y , x / y , x-y


def iterative_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return(total)

def recursive_sum(n):
    if(n == 1):
        return 1
    else:
        return( n + recursive_sum(n-1))

def factorial(factval):
    result = 1
    '''
    #non recursion way
    result = 1
    for i in range(1,factval+1):
        result = result*i
    return result
    '''
    if factval == 0 or factval == 1:
        return 1
    else:
        return(factval * factorial(factval-1))



def nested_function_example():
    print("Within outer function")
    def nested_innerfunc():
        print("Within inner nested function")

    nested_innerfunc() # calling the inner function , not accessible globally
    
def addition_trick_function(value):
    def addition(other_val):
        return value + other_val
    return addition # here returning the function itself

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
    print("Calling overriden round function")
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
