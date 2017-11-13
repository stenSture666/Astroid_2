from polygon import Polygon
from shape import Shape
from point import Point

class Astroid( Polygon ):
    def __init__(self, points=[], x=0, y=0, rotation=0, movement = Point(0,0), ang_vel = 0):
        points = [Point(-15, 0), Point(-10, 10), Point(10, 0), Point(-10, -10)]
        super().__init__(points,x,y,rotation)
        self.pull = movement
        self.angular_velocity=ang_vel