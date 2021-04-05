import time
import random
import sys

while True:
    print('You wake up in a cell. Darkness shreds every inch of your vision. You hear crying in the distance, as the sound echoes through the walls of wherever you find yourself.')
    time.sleep(2)
    print('You stand up. There is a set of 3 lockpicks on your right.')
    time.sleep(2)
    print('Pick up the lockpicks?')
    time.sleep(1)
    print('Y or N')
    #this code is the first player choice
    #remember to do n
    playerChoice1 = input()
    if playerChoice1 == 'n':
        print('A creature comes your way')
        time.sleep(1)
        print('You cant defend')
        time.sleep(1)
        print('You cant fight back')
        time.sleep(1)
        print('Yeah, you dead now')
        break
    elif playerChoice1 == 'y':
        lockcount = 3
        print('Lockpick count = ' + str(lockcount))
        time.sleep(1)
        print('You pick up the lockpicks and go to open the cell door')
        time.sleep(1)
        print('You can hear a faint groaning, but its getting closer. Your hands are shaking')
        time.sleep(5)
        lockchance1 = random.randint (1,10)
    #This code is for the first chance. I dont know the second and third time are working. dont really know how to test it tho
        if lockchance1 != 10:
            print('You successfully lockpick the door')
            lockpick1 = 'yes'
            lockpick2 = 'yes'
            lockpick3 = 'yes'
            lockcount = lockcount - 1
        elif lockchance1 == 10:
            print('You failed the first try')
            lockpick1 = 'no'
            lockcount = lockcount - 1
        #is this the way everyone does things?    
    if lockpick1 == 'no':   
        print('You try again. The groaning is closer this time, and you can see something coming your way. Theres a rock near you. Do you throw it at the thing?')
        playerChoice2 = input()
        if playerChoice2 == 'n'':
            print('The creature is coming. you need to get this lockpick')
            lockchance4 == random.randint(1,11)
            if lockchance4 < 5:
                print('You have successfully opened the lock')                
                lockcount = lockcount - 1                
                lockpick2 == 'yes'                
            elif lockchance4 > 5:
                print('You failed again, and you are down to your last lockpick')
                lockpick2 = 'no'
                lockcount = lockcount - 1                                
        elif playerChoice2 == 'y':
            print('You throw the rock, and miss. But the noise from it makes the creature go to where it landed')
            time.sleep(1)
            print('Because of it, you get a second chance')
            lockchance2 = random.randint (1,10)
            if lockchance2 < 8:
                print ('You successfully lockpick the door')
                lockpick2 = 'yes'
                lockcount = lockcount - 1
            elif lockchance2 > 8:
                print('You failed again, and you are down to your last lockpick')
                lockpick2 = 'no'
                lockcount = lockcount - 1
    if lockpick2 == 'no': 
        print('The creature comes your way.')
        time.sleep(1)
        print('You really need to get this one')
        lockchance3 = random.randint(1,11)
        if lockchance3 < 5:
            print('You have successfully opened the lock')
            lockpick3 = 'yes'
            lockcount = lockcount - 1
        if lockchance3 > 5:
            print('You failed the lockpick,. The creature grabs you from behind. You fight against its graps, but its too strong.')
            time.sleep(2)
            print('You have died')
            lockcount = lockcount - 1
        #funny thing is, it counts the lockpicks, and i have no ideia how to implement a counter
    if lockpick1 == 'yes' or lockpick2 == 'yes' or lockpick3 == 'yes':
        print('You run down the corridor, leaving the creature behind.')
        time.sleep(5)
        print('You get to an intersection. You can go left or right. You can hear a waterfall on the left, but theres birds chirping the other side.')
        time.sleep(2)
        print('Where do you go?')
        time.sleep(1)
        print('Left or Right?')
        playerChoice2 = input()
        if playerChoice2 == 'Left':
            print('You go deeper in the cave, till you reach the waterfall. Theres a chest there. Inside, you find a rusty old sword. You keep to yourself')
            rustysword = 'yes'
            time.sleep(1)
            print('You go back the way you came, and, when you reach the intersection you walk the other way. As you leave the cave, the sunflares on your face. You squinch your eyes. The beaultiful world of (ILL THINK OF SOMETHING). And your adventure starts.')
        elif playerChoice2 == 'Right':
            print('As you leave the cave, the sunflares on your face. You squinch your eyes. The beaultiful world of (ILL THINK OF SOMETHING). And your adventure starts.')
            rustysword = 'no'
time.sleep(3)



#creative ending, i know


