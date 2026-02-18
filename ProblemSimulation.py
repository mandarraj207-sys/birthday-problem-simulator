import random

def found_duplicate(n) :
    birthdays = []
    for i in range(n):
        generated_number = random.randint(1,365)
        if generated_number in birthdays:
            return True
        birthdays.append(generated_number)
    return False  

def simulate(n,runs):
    collisions = 0
    for i in range(runs):
        if found_duplicate(n):
            collisions +=1
    return collisions/runs  