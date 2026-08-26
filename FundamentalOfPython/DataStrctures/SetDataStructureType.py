empty_set = set()
print(empty_set)
print(type(empty_set))

my_prime_set = {1,3,5,7,11}
print(my_prime_set)

my_set = set ([1,1,3,2,2,5,8,5,7,9]) # Remove duplicate itself, as set is unique
print(my_set)

print(set("Hello World!")) # Also it may seems it's ordered , but it's not guaranteed

 # Operation in the set
print(max(my_prime_set)) # same way min()
print(sorted(my_set, reverse=True))

my_set.remove(8) # remove a value | or discard
print(my_set)

# add an element
my_set.add(13)
print(my_set)