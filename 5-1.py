languages = {

		'Jerry Yu': 'run',

		'jerry Chen': 'go',

		'Marco': 'jump',

		'eric': 'fly',

	}

	

members = ['Jerry Yu', 'Jerry Chen', 'eric', 'Marco','Peter', 'Google']

	

for member in members:

	if member in languages.keys():

		print('Thanks for responding, ' + member.title())

	else:

		print('Please take your poll, ' + member.title()) 
rivers = {

		'Yang zi river': 'china',

		 'yellow river': 'china',

		'nile': 'egypt',

		

	}

	

for river, location in rivers.items():

	print('The ' + river.title() + ' is in ' + location.title())

for river in rivers.keys():

	print(river.title())    

for location in rivers.values():

	print(location.title()) 
glossary = {

'toy': 'something meant to be played with, especially by children',

'river': 'a large area of water that flows towards the sea',

'hat': 'a covering for the head, worn for protection from the weather or as a fashion accessory',

'student': 'somebody who studies at a school, college, or university',

'treasure': 'to prize somebody or something as being of great value or worth',

'plain': 'a large expanse of fairly flat dry land, usually with few trees',

'piano': 'a part of a musical composition that is played softly',

'girl': 'a human female from birth until the age at which she is considered an adult',

'boy': 'a young male person',

'joy': 'a feeling of great happiness',

}

	

for item, description in glossary.items():

	print(item + ': ' + description ) 
glossary = {'toy': 'something meant to be played with, especially by children',

'river': 'a large area of water that flows towards the sea',

'hat': 'a covering for the head, worn for protection from the weather or as a fashion accessory',

'student': 'somebody who studies at a school, college, or university',

'treasure': 'to prize somebody or something as being of great value or worth',}

	

print("\n" + 'toy: ' + glossary['toy'])

print("\n" + 'river: ' + glossary['river'])

print("\n" + 'hat: ' + glossary['hat'])

print("\n" + 'student: ' + glossary['student'])

print("\n" + 'treasure ' + glossary['treasure']) 
numbers = {'Jerry': '6', 'Steven': '3', 'Alex': '10', 'Marco': '14', 'Peter': '10' }

	

print('Jerry, ' + str(numbers['sheila']))

print('Steven, ' + str(numbers['joy']))

print('Alex, ' + str(numbers['yoyo']))

print('Marco, ' + str(numbers['jennifer']))

print('Peter, ' + str(numbers['jane']))
ID = {'first_name' : 'Jerry', 'last_name':'Yu', 'age':'15', 'city':'Chengdu'}

print(ID['first_name'])

print(ID['last_name'])

print(ID['age'])

print(ID['city'])
