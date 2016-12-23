class GameObject:
    def __init__(self, img, xPos, yPos, xSpeed = 0, ySpeed = 0):
        self.pos    = img.get_rect().move(xPos, yPos)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.img    = img

    def move(self):
        self.pos = self.pos.move(xSpeed * dT, ySpeed * dT)
