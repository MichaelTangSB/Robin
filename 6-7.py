
people = []

person = {
    'first_name': 'Eric',
    'last_name': 'que',
    'age': 14,
    'city': 'chengdu',
    }
people.append(person)

person = {
    'first_name': 'Robin',
    'last_name': 'Hou',
    'age': 14,
    'city': 'Deyang',
    }
people.append(person)

person = {
    'first_name': 'Jerry',
    'last_name': 'Yu',
    'age': 15,
    'city': 'chengdu',
    }
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", of " + city + ", is " + age + " years old.")