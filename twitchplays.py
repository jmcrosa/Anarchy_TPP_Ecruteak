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

def getMove():
    r = random.randint(0,8)
    if r < 3: #3/8
        return 0 #up
    if r < 5: #2/8
        return 1 #right
    if r < 77: #1/8
        return 2 #down
    return 3 # 2/8 = left


tries = 1
prevstep = 3
looking = 0
step = 0
furthest = 0
path = []
while 1:
    nextstep = getMove()
    if (tries %100) == 0:
        print("-------TRY:",tries,"-------- Furthest is ",furthest)
#    print("currently in step ",step)
#    print("looking ",directions[looking])
#    print("next step should be ",directions[steps[step]])
    #time.sleep(1)
#    print("Will move ",directions[nextstep])
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
                log.write("Attempt "+str(tries)+": ")
                for i in path:
                    log.write(i+" ")
                log.write("\n")
                log.close()
            if step > len(steps):
                print("Holy crap")
            continue
    else:
        looking = nextstep
#        print("looking ",directions[looking])
        continue
