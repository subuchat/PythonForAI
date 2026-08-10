def arithmetic_operations():
    a = 10
    b = 5

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Modulus:", a % b)
    print("Exponentiation:", a ** b)
    print("Floor Division:", a // b)
    print("Hello" + " World")  # String concatenation
    print( True - True)  # Boolean arithmetic
    print(3 ** 4 // 5 % 3)  # Combined arithmetic operations
    print("1 + 3 * 4 / 12 - 6: ", 1 + 3 * 4 / 12 - 6)

def assignment_operations():
    a = 10
    print("Initial value of a:", a)

    a += 5
    print("After a += 5:", a)

    a -= 3
    print("After a -= 3:", a)

    a *= 2
    print("After a *= 2:", a)

    a /= 4
    print("After a /= 4:", a)

def comparison_operations():
    a = 10
    b = 5

    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

def logical_operations():
    a = True
    b = False

    print("a and b:", a and b)
    print("a or b:", a or b)
    print("not a:", not a)

def membership_operations():
    '''
    its a multiline comment for membership operations
    test here if some value is member of a list or not
    '''
    my_list = [1, 2, 3, 4, 5]
    print("Is 3 in my_list?", 3 in my_list)
    print("Is 6 not in my_list?", 6 not in my_list)

def bitwise_operations():
    print("Bitwise Operations with a 10 and b 4:")
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary

    print("a & b:", a & b)  # Bitwise AND
    print("a | b:", a | b)  # Bitwise OR
    print("a ^ b:", a ^ b)  # Bitwise XOR
    print("~a:", ~a)        # Bitwise NOT
    print("a << 1:", a << 1)  # Left shift
    print("a >> 1:", a >> 1)  # Right shift

def test_other():
    a = 'Python'
    b = 'Programming'
    print(a + b * 3)

def main():
    arithmetic_operations()
    assignment_operations()
    comparison_operations()
    logical_operations()
    membership_operations()
    bitwise_operations()
    test_other()

if __name__ == "__main__":
    main()
