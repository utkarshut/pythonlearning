import random

print(random.random())

print(random.uniform(1, 5))

print(random.randint(1, 5))


color =["blue", "red", "green"]

print(random.choice(color))

print(random.choices(color,weights=[18, 18, 2], k=5))

deck = list(range(1,53))

random.shuffle(deck)

print(deck)

hand = random.sample(deck, k=5)

print(hand)