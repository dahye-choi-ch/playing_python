# flip a coin 100 times  - H for each heads and T for each tails
# write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
# the first part generates a list of randomly selected 'heads' and 'tails' values
# the second part checks if there is a streak in it.
# 10000 experiments

def checking_streak(coin_list):
    for index, side in enumerate(coin_list):
        if index==0: pre_side = side; streak_index = 1
        else:
            if side==pre_side:
                streak_index += 1
                if streak_index == 6:
                    return 1;
                    break
            else:
                streak_index = 1;
                pre_side = side
    return 0

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    coins=[]
    for flipping in range(100):
        coins.append( random.randint(0,1) )
    numberOfStreaks += checking_streak( coins )

print('Chance of streak: %s%%' % (numberOfStreaks / 100 ))
