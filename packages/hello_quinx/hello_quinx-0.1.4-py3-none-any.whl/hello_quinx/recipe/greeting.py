from ..core import Person

def hello(person: Person) -> str:
    return f'Hello, {person.name}!'

def hi(person: Person) -> str:
    return f'Hi, {person.name}!'

def whatsup(person: Person) -> str:
    return f'What\'s up? {person.name}'
