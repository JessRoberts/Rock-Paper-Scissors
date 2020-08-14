import random
my_file = open('rating.txt', 'r')
userpick = ''
username = input('Enter your name:')
print('Hello,', username)
score = 0
choices = input()
if choices == '':
    choices = ['rock', 'paper', 'scissors']
else:
    choices = choices.split(",")

for line in my_file:
    line_as_list = line.split()
    rating_name = line_as_list[0]
    if rating_name == username:
        score = int(line_as_list[1])

print("Okay, let's start")

while True:
    userpick = input()
    computer = random.choice(choices)
    wins = []
    loses = []

    if userpick in choices:
        for el in range(choices.index(userpick)):
            wins.append(choices[el])
        for el in range(choices.index(userpick) + 1, len(choices)):
            loses.append(choices[el])
        while len(wins) > len(loses):
            loses.append(wins[0])
            wins.remove(wins[0])
        while len(wins) < len(loses):
            wins.append((loses[-1]))
            loses.remove(loses[-1])

    if userpick == computer:
        print(f'There is a draw ({computer})')
        score += 50
    elif computer in loses:
        print(f'Sorry, but the computer chose {computer}')
    elif computer in wins:
        print(f'Well done. The computer chose {computer} and failed')
        score += 100
    elif userpick == '!rating':
        print('Your rating:', score)
    elif userpick == '!exit':
        print('Bye!')
        exit()
        break
    else:
        print('Invalid Input')
my_file.close()
