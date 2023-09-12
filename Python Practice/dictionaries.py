#Dictionaries
dogs = {
    'Name': 'Daisy',
    'Breed': 'Austrailian Cattle Dog',
    'Skill': 'Speed'
}
print(dogs['Name'])
print(dogs.get('Name'))
print(dogs.pop('Skill'))
print(dogs.popitem())
print('Breed' in dogs)
print(dogs.keys())
print(list(dogs.values()))

dogs['Favorite Toy'] = 'Squeaky Ball'
dogs['Favorite Food'] = 'Homemade Tortillas'

del dogs['Name']
print(dogs)