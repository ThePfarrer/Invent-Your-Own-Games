import random 
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print(f'What is {number1} + {number2}?')
answer = int(input())
if answer == number1 + number2:
    print('Correct!')
else:
    print(f'Nope! The answer is {number1+number2}')