empty_disctionary = {}
empty_disctionary2 = dict() # constructor

print(f"Dictionaries {empty_disctionary} and {empty_disctionary2}")

student_dictionary = {
    'name' : 'Sascha',
    'age'  : 19,
    'sport' : ['football','cricket','swimming']
}
print(student_dictionary)

duplicate_dict = {'A': 1, 'B':3 , 'C': 4 , 'A':5}
print(duplicate_dict)

dictionary_from_ctor = dict(A=1, B=2, C=3)
print(dictionary_from_ctor)

dictionary_from_ctor2 = dict([['a',1],['b',2],['c',3]])
print(dictionary_from_ctor2)

dict_frm_key = dict.fromkeys(['X','Y','Z'], 89 )
print(dict_frm_key)

listKey = ['A','B','C']
listVal = [10,20,30]
print(dict(zip(listKey,listVal)))

new_dict = dict.fromkeys(['A', 'B', 'C'], [[4, 5, 6], [1, -5, 8], [-5, 0, -0]])
print(new_dict)

## Access the disctionary

print(f"Student name is: {student_dictionary['name']}") # Access via key
# SAfer way to access is through get() function. If not there , will return None rather than KeyError
print(f"Student age is {student_dictionary.get('age')}")
print(f"Student Subject is {student_dictionary.get('subjects')}")

# nested dictionary and access
employee_dict = {'emp1014': {'Name': 'Himanshu', 'Department': 'Sales', 'Work Exp': 4},
                 'emp1025': {'Name': 'Jyoti', 'Department': 'Marketing', 'Work Exp': 7},
                 'emp1176': {'Name': 'David', 'Department': 'Category', 'Work Exp': 8}}

# Obtain Jyoti’s work experience
print(employee_dict['emp1025']['Work Exp'])

# Operation of a disctionary

print("Length:", len(dict_frm_key))
print("Length of employee_dict : ", len(employee_dict))

## check memebership or not
print('name' in student_dictionary)    # OR not in

## We can merge 2 or more dictionary ( | )
merged_dict = dictionary_from_ctor | dictionary_from_ctor2 # OR merge and assign |=
print(f"merged of 2 dictionary {dictionary_from_ctor} and {dictionary_from_ctor2} : {merged_dict}")

## Get max value of a Dictionary
scores_of_students = {
    'Amar': 90,
    'Samar': 87,
    'Aakar': 91,
    'Sakaar' : 88
}

max_scorer = max(scores_of_students, key = scores_of_students.get)
print("Maximum number achieved by : ", max_scorer)

# Same way using Lambda function
print(max(scores_of_students, key=lambda person : scores_of_students[person]))
print(f"Value of the max scorer {max_scorer} is {scores_of_students[max_scorer]}")

# sorting by scores/number
print(sorted(scores_of_students, key=scores_of_students.get))

# From nested disctionary

persons_stat = {
    'Alex' :     {'age':30 , 'height': 178},
    'Vivi' :     {'age': 28, 'height': 165},
    'Christian': {'age':29 , 'height':180}
}
print( max(persons_stat)) # only comparing keys

max_height_person = max(persons_stat , key=lambda person : persons_stat[person]['height'])
print(f"Max height's person {max_height_person} and height is {persons_stat[max_height_person]['height']}")