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

# Randomly deletes a number
my_set.pop()
print(my_set)

# Find unique loop from the list
my_list = [1,2,2,3,5, 5, 3, 6, 7, 11, 43, 2]

## convert the list to set and back to list to get the same
my_unq_list = list(set(my_list))
print(my_unq_list)

my_str = "THis is your experiement with set"
print(set(my_str)) # set of unq characters

final_str = ''.join(set(my_str))
print(final_str)

# Union of Set
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
list3 = [3,4,5,6,7]

my_unq_set_4m_list = (set(list1) | set(list2) | set(list3))
print(my_unq_set_4m_list)

## Mathematical operation on Set
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
set3 = {20,30,40}
set4 = {2,3,4}
print("Are these 2 set disjoint :", set1.isdisjoint(set2))
print(f"Are these 2 set{set1} and {set3} disjoint :", set1.isdisjoint(set3))
# To print intersection ( say not disjoint)
print(f"Intersection of {set1} and {set4} is :", set1 & set4)
if( set1 & set4 != {}):
    print("Set1 and set4 are not disjoint")
if(len(set1 & set3) == 0):
    print("set1 and set3 are disjoint")

# Find the intersection
print("Intersection of set1 and set2 :", set1.intersection(set2))
# Subset
print(f"Is {set4} is subset of {set1} :",set4.issubset(set1)) # or check issuperset()
#symetric difference
print("Symetric difference : ", set1.symmetric_difference(set4))
print("Symetric difference : ", set1.symmetric_difference(set2)) # In one of the set but not in both
# Set difference

print(f"Difference of {set1} and {set2} is :", set1-set2)
print("Union: set1 | set2 :", set1.union(set2))

## Set comprehension

sq_set = [i**2 for i in range(1,10)]
print(sq_set)

#  create a list of unique squared values from the list. 
numbers = [1, 2, 3, 4, 5, 2, 3, 4]
print(list({x ** 2 for x in numbers}))
print([x ** 2 for x in set(numbers)])