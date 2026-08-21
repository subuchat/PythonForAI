
empty_string = ''
print(empty_string)

greeting = "Hello World"
print(greeting)

#Both single quote and double quote is same.
# But if you want to show single quote , wrap it up with double quote and vice versa

example = " I'm "
print(example)

name = '"Programmer"'
print(name)

multi_line_str = '''
Hey, this is your 
guide to Python programming.
Go slowly till AI/ML
'''

print(multi_line_str)

# Lets type cast

val = 25
str_val = str(val)
print(type(str_val))
print(str_val)

#Formating string
# %d  decimal , %o octadecimal %x hexadecimal float till 3 digit %.3f
my_int = 25
my_float = 3.1415
formated_str = "The number value %d and float value %.3f ." % (my_int,my_float)
print(formated_str)

another_way_format = "The number {x} and Float val {y:.2f}".format(x=my_int, y=my_float)
print(another_way_format)
print("The number {} and Float val {:.2f}".format(my_int, my_float))
print(f"The number {my_int} and Float val {my_float : .2f}") # formatting to print 2 digit after decimal

# The backslash (\) is used to escape characters in a string, 
# allowing you to include special characters such as \n (new line), \t (tab) and \' (single quote) within the string. 
my_str = "I said \"Hey there\"" # escape character , to include into the string ( here double quote)
print(my_str)

print('Hello\nWorld')

print(len("Hello World"))
#ASCII value
print("ASCII value of A :", ord('A'))

#COncatenation of string

finalval = "Hello" + "World"
print(finalval)

ecstatic = "ha"*5 # 5 times repeat
print(ecstatic)

det_x_is_there = "apple" in "pineapple" # also use 'not in'
print(det_x_is_there)
#chnage case of string by upper()/lower() function
print(finalval.upper())
print(finalval.swapcase())
print(finalval.islower())
message = "asdfgh23456"
print(message.isalpha())
#string contain digit/alphabet
my_num = "12345"
print(my_num.isdigit())
print(message.index('g')) #starts from 0
print(message.find('g')) 
print(message.find('x'))  # will return -1 if not found
print(finalval.count('l'))
print(finalval.replace('Hello','Hi'))
print(finalval)

#split it with default space character to make list
my_msg = "we are here for python"
split_string = my_msg.split()
print(split_string)
# remove leading/trailing white space by strip() function
message = "       is it so!       "
print(message.strip()) # use lstrip() for only leading one and rstrip() for only trailing one

joined_str = ' '.join(split_string) # Given space for every splitted string to join
print(joined_str)

print(my_msg.capitalize()) # First letter of the string to become capital
print(my_msg.title()) # The .title() method converts the first character of each word in a string to uppercase and the rest to lowercase.

#Slice a string , or you can get by index my_msg[15] or string[start index : end index]
temp_msg = my_msg[3:15] # 15-1 = 14th index
print(temp_msg)
#print last character
print(my_msg[-1])
print(finalval[-4:]) # 4th char from last till end
# string[ start index : end index : steps]
print(my_msg[ : :2]) # start to end with every second char
print(finalval[: : -1]) # recerve the string

my_string = 'Hello, World!'
print(my_string[7:12])