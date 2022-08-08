import random

def guess():
    x = int(input("please enter a number as guess upper bound: "))
    random_number = random.randint(1, x)
    guess = -100
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("please try a larger one")
        elif guess > random_number:
            print("please try a smaller one")
    print("congrats!!!! you got it!!")

def computer_guess():
    x = int(input('pls enter a number as a guess upper bound: '))
    low = 1
    high = x
    feedback = ''
    while feedback != 'correct':
        guess = random.randint(low, high)
        feedback = input(f'is {guess} s(smaller) or l(larger) than answ or c(correct): ').lower()
        ##enter s(smaller) or l(larger) or c(correct)

        if (feedback == 'l'):
            high = guess - 1
        elif feedback == 's':
            low = guess + 1
        else:
            print('congrts!! You are a smart computer!!')
            feedback = 'correct'

def guess_num_game():
    user_input = input('you guess or computer guess?(enter me if you want to play or c means computer guess): ')
    if user_input == 'me':
        guess()
    else:
        computer_guess()

guess_num_game()