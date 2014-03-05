class Player:
    Directions = { "up" : 0,
                   "right" : 1,
                   "down" : 2,
                   "left" : 3 }
    startX = 4
    startY = 12
    startFacing = Directions["up"]

    def Reset(self):
        self.locX = Player.startX
        self.locY = Player.startY
        
        self.facing = Player.startFacing

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
            if (direction == Player.Directions["up"]):
                self.locY -= 1
            elif (direction == Player.Directions["right"]):
                self.locX += 1
            elif (direction == Player.Directions["down"]):
                self.locY -= 1
            elif (direction == Player.Directions["left"]):
                self.locX -= 1
        else:
            # Not looking this way, look this way now
            self.facing = direction

    def GetPosition(self):
        return (self.locX, self.locY)
