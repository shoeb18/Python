# dictionary methods

my_dict = {
    'name' : 'Shoeb',
    'age' : 19,
    'hobby': 'Gaming'
}

# prints the all keys of dictionary
print(my_dict.keys())

# prints the all values of dictionary
print(my_dict.values())

# prints the all key-value pair of dictionary
print(my_dict.items())

# update the old dict to new dict
new_dict = {
    'favLang' : 'python',
    'hobby' : 'sketching'
}
my_dict.update(new_dict)
print(my_dict)



# get()

# Return the value for key else return None
print(my_dict.get('player'))

# Return the value for key else throws an error if key is not present
print(my_dict['player'])