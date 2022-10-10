import random
from people import Person, Action

list = Person()
people = Person(name='Yoru', health_status=100, mood=100, capital=0)

print(people)


people.change_state(
    capital=random.randint(50, 100),
    mood=random.randint(-20, -10),
    health_status=random.randint(-10, -5)
)

people.change_state(
    capital=random.randint(-40, -20),
    mood=random.randint(30, 100),
    health_status=random.randint(50, 100)
)
print(people)