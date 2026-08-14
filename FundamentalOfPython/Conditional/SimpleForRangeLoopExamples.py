def main():
    simple_for_range_loop()
    for_range_loop_with_continue()
    for_range_loop_with_break()
    test_for_range_loop()
    test_with_range_conditional()
    test_with_brak_continue()
    nested_loop_example()
    example_with_forLoop()

def example_with_forLoop():
    '''
    for i in range(2):
        for j in range(3):
            print('i =', i, 'j =', j)
    '''
    tmp = ''
    while True:
        if tmp == 'hhh':
            break
        for ch in 'Python':
            if ch == 'h':
                tmp += ch
        print(tmp)

def nested_loop_example():
    n = 6
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ') # surpassing default new line to make space between numbers
        print()  # for new line after each row

def test_with_brak_continue(): # So that 'X' never print
    for x in 'PythXn':
        if x == 'X':
            break
        print(x)
        continue
        print('X')

def test_with_range_conditional():
    for ch in 'Pantalaimon': 
        print(ch) if ch != 'a' else print()

def test_for_range_loop():
    #for i in range(12,1,-2): #both correct
    for i in range(12,0,-2):
        print(i)

def simple_for_range_loop():
    for count in range(5):
        print(f'Count is: {count}')

def for_range_loop_with_continue():
    for count in range(10): #value will take from 0-9
        if count % 2 == 0:
            continue   #it will not print even value and continue to loop
        print(f'Odd number is: {count}')

def for_range_loop_with_break():
    for count in range(10):
        if count == 5:
            break   #it will stop the loop when count is 5
        print(f'Count is: {count}') 


if __name__ == "__main__":
    main()
