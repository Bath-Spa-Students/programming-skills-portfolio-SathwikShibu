pets = []


pet = {
    'animal type': 'python',
    'name': 'viperion',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'tiger',
    'name': 'sher khan',
    'owner': 'Badshah',
    'weight': 45,
    'eats': 'meet',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'luffy',
    'owner': 'Tom',
    'weight': 16,
    'eats': 'fish',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")