import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print(f'900 flips and there have been {heads} heads')
    if flips == 100:
        print(f'At 100 tosses, heads has come up {heads} times so far.')
    if flips == 500:
        print(f'Halfway done, and heads has come up {heads} times.')

print()
print(f'Out of 1000 coin tosses, heads came up {heads} times!')
print('Were you close?')
