import Gym, Player, random

player = Player.Player()
gym = Gym.Gym()

greatest = -1

for i in range(1,1000000):
    visited = []

    while True:
        move = random.randint(0, 3)

        state = player.Move(move)

        if state == 0:
            # Invalid move, move them back
            player.Undo()
        elif state == 2 or state == -1:
            # Fell to our death, reset
            break
        elif state == 4:
            # Holy crap we made it
            print("Holy shit")
            break

        if player.locY < player.startY and player.GetPosition() not in visited:
            visited.append(player.GetPosition())

    if len(visited) > greatest:
        print("Attempt", i, "ended, visiting", len(visited), "invisible tiles.")
        print("\t", player.path)
        greatest = len(visited)

    player.Reset()
