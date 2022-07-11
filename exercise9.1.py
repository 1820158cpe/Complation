try:
    person = {
        'first_name': 'John',
        'last_name': 'Cuenca',
        'age': 21,
        'city': 'Lipa',
        }

    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
except:
    print('Error! Person not found')