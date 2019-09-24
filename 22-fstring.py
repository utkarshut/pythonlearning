fname = 'ut'
lname = 'bhardw'

print(f'my name is {fname.upper()} {lname.lower()} ')

person = {'name': 'john', 'age': 23}


print(f"mine name {person['name']} age {person['age']}")


for n in range(1,5):
    print(f"number is {n:04}")


pi = 3.141586


print(f'pi is {pi:.3f}')

from datetime import datetime

dob = datetime(1993, 9, 10)

print(f'birthday is {dob: %B %d, %Y}')