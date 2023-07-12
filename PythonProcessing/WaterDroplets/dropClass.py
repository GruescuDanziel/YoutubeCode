class Drop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        
    def grow(self):
        self.radius += 1
        
    def drawCircle(self):
        stroke(255-self.radius)
        if self.radius < 255:
            circle(self.x, self.y, self.radius)
            self.grow()
