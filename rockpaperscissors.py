import random

options = ('rock', 'paper', 'scissors')
player = None
computer = random.choice(options)


while player not in options:
    player = input("Enter your choice(rock, paper, scissors): ")

print(f'Player: {player}')
print(f"Computer: {computer}")


if player == 'paper' and computer == 'rock':
    print(f"You are win!")
elif player == 'rock' and computer == 'paper':
    print(f"You are lost!")
elif player == 'scissors' and computer == 'rock':
    print(f"You are lost!")
elif player == 'rock' and computer == 'scissors':
    print(f'You are win!')
elif player == 'scissors' and computer == 'paper':
    print(f"You are win!")
elif player == 'paper' and computer == 'scissors':
    print(f"You are lost!")
else:
    print('Match Tie')


print(f"--------------------------")
print(f"--- Thanks For playing ---")
print(f"--------------------------")