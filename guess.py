# Blog: guoj.org
# Github: github.com/guojing0
# Email: dev.guoj@gmail.com

import simplegui
import random, math

num = 100 # init the num for a new game

def new_game():
    global num_of_guesses, secret_number
    num_of_guesses = int(math.ceil(math.log(num, 2)))
    secret_number = random.randrange(0, num)

    print 'New game ranging from 0 to', num
    print 'Number of remaining guesses is', num_of_guesses, '\n'

def range100():
    global num
    num = 100
    new_game()

def range1000():
    global num
    num = 1000
    new_game()

def input_guess(guess):
    global num_of_guesses
    num_of_guesses -= 1
    print 'Guess was', guess
    print 'Number of remaining guesses is', num_of_guesses

    if num_of_guesses <= 0:
        print 'You ran out of guesses. The number was', secret_number, '\n'
        new_game()
    elif int(guess) > secret_number:
        print 'Lower!\n'
    elif int(guess) < secret_number:
        print 'Higher!\n'
    else:
        print 'Correct!\n'
        new_game()

frame = simplegui.create_frame('Guess the Number', 300, 300)
frame.add_input('Input', input_guess, 150)
frame.add_button('Range: 0 - 100', range100, 150)
frame.add_button('Range: 0 - 1000', range1000, 150)
frame.start()

new_game()
