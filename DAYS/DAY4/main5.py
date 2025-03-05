# index Errors 
# Nested List

flowers = ["rose", "lily", "sunflower",'carnation','jasmine','daisy']

length = len(flowers)
print(length)

# IndexError: list index out of range
# print(flowers[length])


# Nested list
male_names = [ "sanjay","vikas","rohit","abhishek"]

female_names = [ "meenu", "siddhi", "priyanka", "malvika"]

person_name = [male_names, female_names]

print(person_name)
print()


print(f'male name: {person_name[0]}')
print()
print(f'female name: {person_name[1]}')
