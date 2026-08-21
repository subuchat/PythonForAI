
empty_list =[]

my_lst = [1, 5, 2, 'A','H', 9]
print(my_lst)

print("Hello World!".split()) # Will generate list separating space ( if any other , need to provide the same in split() arg)
print(list("Hello World")) # Generate list of all the character

num_list = list(range(1,10))
print(num_list)

nested_list = [1, [2,3], [4,5,6], [7,8]]

# Indexing and slicing of the list

print(nested_list[2])

print(num_list[-1]) # Get the last element of the list

# slice of the list

sliced_lst = num_list[2:7:2] # Start = 2 , end - (7-1) , taking 2nd value
print(sliced_lst)

print(num_list[::-1]) # reverse the list

print(sum(num_list)) # can be sum-ed if it is a mathematical list

unsorted_lst = [2,9,5,1,4,5,11]
print(sorted(unsorted_lst)) # sort the list ascending order
print(sorted(unsorted_lst, reverse= True)) # sort the list in descending order
print("Length of the numbered list: ",len(num_list))


# Zip function
# It allows two or more iterable sequence into a single iterable sequence. 
# This is valueable when you want to iterate over multiple iterable sequence at the same time. Resulting in Tuple

name_lst      = ['Ram', 'Alex','Dave','Vivi']
country_list  = ['IND', 'GER','USA','CHN']

zipped_lst = zip(name_lst,country_list)
print(zipped_lst) # It will resulting in tuple/ shows zip object

# to view call list function on the zipped list

saved_zipped = list(zipped_lst)

# Iterate over the list/zipped list

'''
A zipped list cannot be accessed again after printing because zip() returns an iterator. 
Iterators are designed for one-time use; once you loop through or consume the items (such as during a print() call), 
the iterator becomes empty and yields no more values.
If needed , save the zip list to a new variable like saved_zipped above

How Zip WorksLazy evaluation: 
    It generates items on the fly instead of storing them in memory.
    Single pass: It moves forward through the data and forgets previous items.
    Exhaustion: Printing or converting it uses up the data.
How to Fix ItConvert to a list: 
    Wrap the zip object in list() to save it in memory.
    Reuse the list: You can print and access a true list many times.

'''
for name , country in saved_zipped:   # Using saved_zippped instead of zipped_list , as its gets printed once
    print("Listing Name and country of the data")
    print(f"{name} is from Country {country}")

# Method of List

## Find Index of an element in the list

print("Index in Dave in the list : ", name_lst.index('Dave'))

# Search where is he maximum element lies in the list
print( unsorted_lst.index ( max(unsorted_lst)) )

# LEts change the list

unsorted_lst.append(12) # add it at the end of list
print(unsorted_lst) # changed inplace
unsorted_lst.insert(3 , 15) # insert in 3rd index value 15
print(unsorted_lst)
# remove last value by pop() function , any particular item can be delete4d by remove(value) call
popped_val = unsorted_lst.pop()
print(f" Deleted the last value {popped_val} from {unsorted_lst}")

# sort/reverse/append - at the end/insert - position/remove - item/pop - last value OR can tell the index functions can also be done in the list
#lst.clear() - will remove everything of the list
# You can add more than one value together , but extend in list way

unsorted_lst.extend([12, 32])
print(unsorted_lst)


popped_particular_index_val = unsorted_lst.pop(3)
print(f"4th Value of the {unsorted_lst} was : {popped_particular_index_val}")

# Extend or + operator - both can add in the list

final_list = unsorted_lst + [76,1]
print(final_list)

########## Write a program to remove consecutive duplicate from the list #################

list_with_duplicateItems = [1, 2 , 2, 5, 5, 3, 3, 3, 2, 9, 12, 12]
modified_unque_list = [list_with_duplicateItems[0]] #start with first item in the list and then start with next( index 1 in the loop)

for index in range(1,len(list_with_duplicateItems)):
    if list_with_duplicateItems[index] != list_with_duplicateItems[index-1]:
        modified_unque_list.append(list_with_duplicateItems[index]) # add into modified list if its not previous value

print(f" Unique list from {list_with_duplicateItems} is : {modified_unque_list}")


####################

# make cubes of existing numbered list
print(num_list)

cubed_list = [ val**3 for val in num_list]
print(f"Cube list of {num_list} is {cubed_list}")