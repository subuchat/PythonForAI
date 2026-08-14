
def simple_if_else():
    a = 12
    b = 20
    c = 15

    if a < b:
        result = 'a is smaller than b'
    elif a == b:
        result = 'a is equal to b'
    elif a < c:
        result = 'a is smaller than c'
    else:
        result = 'a is the largest'

    print(result)

def nested_if_else():
    membership_status = 'active'
    late_fees = 20
    book_available = True

    if membership_status == 'active':
        if late_fees == 0:
            if book_available:
                print('You can borrow the book!')
            else:
                print('Sorry, the book is not available.')
        else:
            print('You have outstanding late fees.')
    else:
        print('Your membership is inactive.')

#In Python's match-case statement, the case blocks are evaluated in the order they are written, 
# and once a match is found, the remaining cases are skipped.

def match_case_example():
    day = 'Monday'

    match day:
        case 'Monday':
            print('Start of the work week.')
        case 'Tuesday':
            print('Second day of the work week.')
        case 'Wednesday':
            print('Midweek day.')
        case 'Thursday':
            print('Almost the weekend.')
        case 'Friday':
            print('Last workday of the week.')
        case 'Saturday' | 'Sunday':
            print('It\'s the weekend!')
        case _:
            print('Invalid day.')

#Guard Cluse - Conditional within a case statement, allows for more complex matching conditions and can be used to filter cases based on additional criteria.

def match_case_with_multivalue_wth_GuardClause():
    x = int(input("Input X co-ordinate: "))
    y = int(input("Input Y co-ordinate: "))

    match (x, y):
        case (0, 0):
            print('Origin')
        case (0, y) if y > 0:
            print('Positive Y-axis')
        case (0, y) if y < 0:
            print('Negative Y-axis')
        case (x, 0) if x > 0:
            print('Positive X-axis')
        case (x, 0) if x < 0:
            print('Negative X-axis')
        case (x, y) if x > 0 and y > 0:
            print('First quadrant')
        case (x, y) if x < 0 and y > 0:
            print('Second quadrant')
        case (x, y) if x < 0 and y < 0:
            print('Third quadrant')
        case (x, y) if x > 0 and y < 0:
            print('Fourth quadrant')
        case _:
            print('Invalid coordinates')

def main():
    simple_if_else()
    nested_if_else()
    match_case_example()
    match_case_with_multivalue_wth_GuardClause()

if __name__ == "__main__":
    main()