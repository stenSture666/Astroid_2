from circle import Circle

class Bullet(Circle):
    def __init__(self, x=0, y=0, r=1, rotation=0):
        super().__init__(x,y,r,rotation)
        self.accelerate(2)




