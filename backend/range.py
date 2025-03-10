import poker
import random

utg = poker.hand.Range("A9s+ AQo+ 66+ KQs+ QJs+ JTs+ T9s 98s A5s")
print(utg.to_ascii().split())

allhands = poker.hand.Range("XX").to_ascii().split()

print(random.choice(allhands))


if 'A8s' in utg.to_ascii().split():
    print("yay")
    
    
