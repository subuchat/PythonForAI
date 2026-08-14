
def main():
    check_age_example()
    check_if_string_is_palindrome()
    reverse_string()
    just_test()
    vowel_remover_editor()

def vowel_remover_editor():
    '''
    This function removes vowels from a given string and prints the modified string.
    OPtion 1
    '''
    input_string=input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    output_string = ''

    for char in input_string: 
        if char not in vowels:
            output_string += char

    print(output_string)

    '''
    # Option 2
    '''

    input_string=input("OP2 : Enter a string: ")
    output_string = ''

    for char in input_string:
        if char in 'aeiouAEIOU':
            continue 
        output_string += char

    print(output_string)

    #Option 3
    input_string=input("Op3 : Enter a string: ")
    output_string = ''

    for char in input_string:
        if char not in 'aeiou': # not correct ,this the string
            output_string += char 

    print(output_string)


def just_test():
    input_str = "I love programming in python"

    count=0    # initializing count variable

    l = ['a', 'e', 'i', 'o', 'u']

    m = ['y']

    # Converting the string to lowercase

    for i in input_str.lower():

        if i in l:

            count = count+1

        if i in m:

            count = count-1

    print(count)

def reverse_string():
    input_string = 'hello'
    new_string = ''

    for char in input_string:
        new_string = char + new_string 

    print(new_string)


def check_if_string_is_palindrome():
    string = input("Enter a string: ")
    reversed_string = string[::-1]

    if string == reversed_string:
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')

def check_age_example():
    age = 1

    while True:
        if age>=19: break
        print(age, "years old. Children not allowed.")
        age=age+1

if __name__ == "__main__":
    main()
