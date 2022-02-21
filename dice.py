#kaitlyn bauer
#dice game

from random import randint 
from time import sleep

budget = 100

def get_user_wager():
    print('Your wager is:' +str(user_wager))
    return user_wager

def get_user_guess(): #defining fuction
    user_guess = int(input('Choose a number 2-12. What is your guess: '))
    sleep(2)
    print("You chose: " + str(user_guess))
    return user_guess

def roll_dice(user_wager, budget): #defining function
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total = first_roll + second_roll
    sleep(1)
    user_guess= get_user_guess()
    
    
    if user_wager > budget or user_wager <1:
        print('Insufficient Funds')
    elif user_guess >= 12 and user_guess <2:
        sleep(2)
        print("Guess Invalid")
    else:
        print('Rolling...')
        sleep(2)
        print('First roll is: ' + str(first_roll))
        sleep(1)
        print('Second roll is: ' + str(second_roll))
        sleep(1)
        print('The house roll is: ' + str(total))
    
    if user_guess == total:
        print('You win!')
        sleep(2)
        budget = user_wager *12
        print('Your total is: ' + str(budget))
        return budget
    
    else:
        sleep(2)
        print('You lose')
        return -user_wager

choice= input("Welcome to Kaitlyn's casino, do you want to play the dice game?: ")

while budget <= 100 and choice =='yes':
    sleep(1)
    user_wager = int(input("Let's make a wager(pick a number less than your less than your budget): "))
    roll_dice(user_wager, budget)
    budget = budget + roll_dice(user_wager, budget)
    print('Your total is:' + str(budget))
    user_choice = input('If you want to keep playing press enter. If you want to quit press 0')
    if user_choice == '0':
        break
    if budget <= 0:
        break

while choice =='no':
    print("Thanks for stopping by Kaitlyn's Casino")
    break
