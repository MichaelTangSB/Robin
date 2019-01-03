pets = []

pet = {
    'animal type': 'scp-683',
    'name': 'father',
    'owner': 'Robin',
    'weight': 14432,
    'eats': 'everything',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'blaalla',
    'owner': 'tiffany',
    'weight': 412534,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'klpp',
    'owner': 'eric',
    'weight': 32,
    'eats': 'brains',
}
pets.append(pet)

for pet in pets:
    print(pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))