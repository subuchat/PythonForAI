
def main():
    simple_while_loops()
    while_loops_with_continue()
    while_loops_with_break()
    test_while_loop()

def test_while_loop():
    my_str = '12345678'
    x = '1'

    while x in my_str:
        print(x)
        x += str(int(x) + 1)

def simple_while_loops():
    count = 0
    while count < 5:
        print(f'Count is: {count}')
        count += 1

def while_loops_with_continue():
    count = 0
    while count < 10:
        count += 1
        if count % 2 == 0:
            continue   #it will not print even value and continue to loop
        print(f'Odd number is: {count}')

def while_loops_with_break():
    count = 0
    while count < 10:
        count += 1
        if count == 5:
            break         #break and come out of loop when count is 5
        print(f'Count is: {count}')

if __name__ == "__main__":
    main()