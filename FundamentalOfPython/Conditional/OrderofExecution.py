# Python code execute from left to right , from top to bottom

print("This is the first line of code")
print("This is the second line of code")

#left to right execution
val = 100 /10 /2
print(val)

# to the power execuute from right to left
tothepower = 2**3**2
print(tothepower)

# Check operator precedence , multiply and divide have same precedence , so they will be executed from left to right
result = 10 + 20 * 30 / 5
print(result)

result = True or False and not False # not has higher precedence than and , so it will be executed first
print("True or False and not False:", result)

#With parentheses , the expression inside parentheses will be executed first
result = (10 + 20) * 30 / 5
print(result)

val = 100 / (10 / 2)
print(val)