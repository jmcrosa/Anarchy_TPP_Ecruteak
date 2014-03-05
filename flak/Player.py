import Gym

class Player:
    Directions = { "up" : 0,
                   "right" : 1,
                   "down" : 2,
                   "left" : 3 }
    hack = ["up", "right", "down", "left"]
    
    startX = 4
    startY = 12
    startFacing = Directions["up"]

    def Reset(self):
        self.locX = Player.startX
        self.locY = Player.startY
        
        self.facing = Player.startFacing
        self.path = ""

    def __init__(self):
        self.Reset()

    def Undo(self):
        self.locX = self.lastX
        self.locY = self.lastY

    def Move(self, direction):
        self.lastX = self.locX
        self.lastY = self.locY
        
        if direction == self.facing:
            # Already looking this way, move a tile
            peekX = self.locX
            peekY = self.locY
            
            if (direction == Player.Directions["up"]):
                peekY -= 1
            elif (direction == Player.Directions["right"]):
                peekX += 1
            elif (direction == Player.Directions["down"]):
                peekY += 1
            elif (direction == Player.Directions["left"]):
                peekX -= 1

            result = Gym.Gym.GetTile(peekX, peekY)

            if result == 1:
                # valid move
                self.locX = peekX
                self.locY = peekY
                self.path += Player.hack[direction] + " "
            elif result == -1 or result == 2:
                self.path += "{" + Player.hack[direction] + "}"

            return result
        else:
            # Not looking this way, look this way now
            self.facing = direction

    def GetPosition(self):
        return (self.locX, self.locY)
