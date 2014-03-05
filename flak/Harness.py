import Gym, Player, random

player = Player.Player()
gym = Gym.Gym()

hack = ["up", "right", "down", "left"]

greatest = -1

for i in range(1,1000000):
    visited = []
    path = ""

    while True:
        move = random.randint(0, 3)

        player.Move(move)

        state = gym.GetTile(player.GetPosition())

        if state == 0:
            # Invalid move, move them back
            player.Undo()
        elif state == 2:
            # Fell to our death, reset
            break
        elif state == 4:
            # Holy crap we made it
            print("Holy shit")
            break

        path += hack[move] + " "

        if player.locY < player.startY and player.GetPosition() not in visited:
            visited.append(player.GetPosition())

    if len(visited) > greatest:
        print("Attempt ", i, "ended at", player.GetPosition())
        print("\tvisited", len(visited), "unique tiles.")
        print("\tpath", path)
        greatest = len(visited)

    player.Reset()
