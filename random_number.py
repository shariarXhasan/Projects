import random

first_num = 0
second_numb = 100

answer = random.randint(first_num, second_numb)
guesses = 0

is_running = True

print('---------NUmber Guessing Game---------')
print(f'Select a number between {first_num} and {second_numb}')



while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1


        if guess < first_num and guess > second_numb:
            print(f"That's number is out of range.")
            print(f'Select a number between {first_num} and {second_numb}')

        elif guess < answer:
            print("Too low") 
        elif guess > answer:
            print("TOO high")
        else:
            print(f"Correct")
            print(f"NUmber is {answer}")
            print(f"Number fo {guesses}")



    else:
        print('Invalid Guess')
        print(f'Select a number between {first_num} and {second_numb}')
