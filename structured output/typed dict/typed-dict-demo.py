from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int
    

person = {
    'name' : 'shravan',
    'age' : 21
}

person1 = Person(**person)
print(person1['name'])
print(person1['age'])
print(person1)