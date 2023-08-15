#           Python Begineer Boost

#           Random Module

import random

random_integer = random.randint(1,100)
print("Random Integer ", random_integer)


fruits = ["apple","banana","orange","cherry","watermelon"]
random_fruit = random.choice(fruits)
print("random fruit",random_fruit)

deck_of_cards = ["Ace","1","2","3"]
print(deck_of_cards)
random.shuffle(deck_of_cards)
print(deck_of_cards)

coin_side = ["Heads","Tails"]
print(random.choice(coin_side))

print(random.randint(1,6))