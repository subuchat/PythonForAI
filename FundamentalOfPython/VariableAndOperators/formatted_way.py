import sys

    
def get_user_name():
    return input("What is your name? ") # this will always be str type

def print_random_test():
    print("abc")
    print(1,2,3)
    print(True)

def test_none_type():
    var = None  # typecasted to None
    print(var)  # This will print None
    print(type(var))  # This will print <class 'NoneType'>
    print(str(var))  # This will print 'None'

def main():
    print(sys.version)  # This is a comment
    # Input user name and greet them
    user_name = get_user_name()
    print(f"Hello, {user_name}!")  # This is another comment   
    print_random_test()
    test_none_type()

if __name__ == "__main__":
    main()
