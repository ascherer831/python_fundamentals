# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x = [ [5,2,3], [10,8,9] ] 
# def change_x(x):
#     x[1][0]=15
#     return x
# print(change_x(x))

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# def change_last(x):
#     students[0]['last_name'] = "Bryant"
#     return students
# print(change_last(students))

# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# def change_name(x):
#     sports_directory['soccer'][0] = 'Andres'
#     return sports_directory
# print(change_name(sports_directory))

# Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]

# def change_y(z):
#     z[0}['y']=30
#     return z
# print(change_y(z))

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterate_dictionary(some_list):
#     for i in students:
#         print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
# print(iterate_dictionary(students))

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students)

# def iterate_dictionary2(key_name, some_list):
#     for i in some_list:
#         print(i[key_name])
# iterate_dictionary2('first_name', students)
# iterate_dictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for k, v in some_dict.items():
        print(len(v), k.upper())
        for i in range(len(v)):
            print(v[i])


print_info(dojo)


