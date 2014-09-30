# Blog: guoj.org
# Github: github.com/guojing0
# Email: dev.guoj@gmail.com

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

dict_name_to_num = {"rock": 0, "Spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
dict_num_to_name = {0: "rock", 1: "Spock", 2: "paper", 3: "lizard", 4: "scissors"}

def name_to_number(name):
    return dict_name_to_num[name]

def number_to_name(number):
    return dict_num_to_name[number]

def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    print "Player chooses %s" % player_choice

    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses %s" % comp_choice

    diff_mod = (player_number - comp_number) % 5
    if 1 <= diff_mod <= 2:
       print "Player wins!\n"
    elif 3 <= diff_mod <= 4:
       print "Computer wins!\n"
    else:
       print "Player and computer tie!\n"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")