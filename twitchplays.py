#twitchplays.py

import random
import time
directions = ['up','right','down','left']
steps = [0,1,1,0,0,0,3,3,3,0,0,0,1,1,1,0,0,3,0,0]
up =3
down= 1
left = 2
right = 2
obstacles = []
for i in range(len(steps)):
    obstacles.append(4)
obstacles[0] = 3
obstacles[5] = 1
obstacles[10] = 3
obstacles[15] = 1

#direction changes:
#starts up
#1-> right
#3->up
#6->left
#9->up
#12->right
#15->up
#17->left
#18->up

#Assume: 40% trolls. (push off path)
#Asume: 40% actually do it in the right direction
#Assume: 20% backtrack

def getMove(target):
    r = random.randint(0,8)
    odds = [2,2,2,2]
    if target < 1:          #favor up
        odds = [3,2,1,2]
    elif target < 4:        #favor right
        odds = [2,3,1,2]
    elif target < 7:        #favor up
        odds = [3,2,1,2]
    elif target < 10:       #favor left
        odds = [2,1,3,2]
    elif target < 13:       #favor up
        odds = [3,2,1,2]
    elif target < 16:       #favor right
        odds = [2,3,1,2]
    elif target < 18:       #favor up
        odds = [3,2,1,2]
    elif target < 19:       #favor left
        odds = [2,1,3,2]
    else:                   #favor up
        odds = [3,2,1,2]

    if r < odds[0]:
        return 0
    if r < odds[0]+odds[1]:
        return 1
    if r < odds[0]+odds[1]+odds[2]:
        return 2
    return 3

simulations =1
while True:
    log = open("best_paths.txt","a")
    log.write("------------- SIMULATION "+str(simulations)+"------------\n")
    log.close()
    tries = 1
    prevstep = 3
    looking = 0
    step = 0
    furthest = 0
    path = []
    moves = 0
    while True:
        nextstep = getMove(step)
        moves += 1
        if (moves%10000000) == 1:
            print("-------SIM #",simulations,"TRY:",tries,"-------- Furthest is ",furthest)
            log = open("best_paths.txt","a")
            log.write(time.asctime()+" STATUS: Try #"+str(tries)+" Furthest is "+str(furthest)+"\n")
            log.close()
        if nextstep == looking:
            if steps[step]!=nextstep:
                if nextstep == obstacles[step]:
    #                print("tried to run into an obstacle")
                    continue
                if step > 1 and nextstep == ((prevstep+2)%4):
    #                print("Moved back ",directions[nextstep])
                    step = step-1
                    path.append(directions[nextstep])
                    if step < 0:
    #                    print("went off initial area")
                        step = 0
                        tries = tries + 1
                        path = []
                    continue
                else:
    #                print("Fell down in step ",step)
                    tries = tries +1
                    step = 0
                    path = []
                    continue
            else:
    #            print("moved ",directions[nextstep])
                path.append(directions[nextstep])
                prevstep = nextstep
                step = step+1
                if step > furthest:
                    furthest=step
                    log = open("best_paths.txt","a")
                    log.write(time.asctime())
                    log.write(": Attempt "+str(tries)+": ")
                    log.write(str(furthest)+"/"+str(len(steps))+" steps: ")
                    for i in path:
                        log.write(i+" ")
                    log.write("\n")
                    log.close()
                if step > len(steps):
                    print("Holy crap")
                    break
                continue
        else:
            looking = nextstep
    #        print("looking ",directions[looking])
            continue
