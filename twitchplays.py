#twitchplays.py

import random
import time
directions = ['up','right','down','left']
steps = [0,1,1,0,0,0,3,3,3,0,0,0,1,1,1,0,0,3,0,0]
obstacles = []
for i in range(len(steps)):
    obstacles.append(4)
obstacles[0] = 3
obstacles[5] = 1
obstacles[10] = 3
obstacles[15] = 1

tries = 1

prevstep = 3
looking = 0
step = 0
furthest = 0
while 1:
    print("-------TRY:",tries,"-------- Furthest is ",furthest)
    print("currently in step ",step)
    print("looking ",directions[looking])
    print("next step should be ",directions[steps[step]])
    nextstep = random.randint(0,3)
    #time.sleep(1)
    print("Will move ",directions[nextstep])
    if nextstep == looking:
        if steps[step]!=nextstep:
            if nextstep == obstacles[step]:
                print("tried to run into an obstacle")
                continue
            if steps[step-1] == ((nextstep+2)%4):
                print("Moved back ",directions[nextstep])
                step = step-1
                if step < 0:
                    print("went off initial area")
                    step = 0
                    tries = tries + 1
                continue
            else:
                print("Fell down in step ",step)
                tries = tries +1
                step = 0
                continue
        else:
            print("moved ",directions[nextstep])
            step = step+1
            if step > furthest:
                furthest=step
            if step > len(steps):
                print("Holy crap")
            continue
    else:
        looking = nextstep
        print("looking ",directions[looking])
        continue
