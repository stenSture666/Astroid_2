import sys
import random
import pygame
import math
import time
from pygame.locals import *
from ship import Ship
from astroid import Astroid
from star import Star
from bullet import Bullet
from game import Game
from point import Point


class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """
    def __init__(self, name, width, height):
        super().__init__( name, width, height )
        pygame.init()  # to enable timer
        self.ship = Ship() #  TODO: should create a Ship object here
        # TODO: should create asteroids
        astroids = [Astroid(x=150,y=300,movement=Point(1,1),ang_vel=1),Astroid(x=50,y=100,movement=Point(1,-1),ang_vel=1),Astroid(x=400,y=400,movement=Point(-1,1),ang_vel=-1)]
        self.asteroids= astroids
        # TODO: should create stars
        stars = []
        for i in range(10):
            for j in range (8):
                stars.append(Star(x=i*64,y=j*64))
        self.stars=stars
        bullets=[]
        self.bullets = bullets

    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-3)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(3)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.05)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:

                bullet = Bullet()
                bullet.timer = pygame.time.get_ticks()
                bullet.position=self.ship.position
                bullet.pull.x = (2 * math.cos(math.radians(self.ship.rotation)))
                bullet.pull.y = (2 * math.sin(math.radians(self.ship.rotation)))
                self.bullets.append(bullet)
            # TODO: should create a bullet when the user fires



    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """
        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )
        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
        for star in self.stars:
            star.update( self.width, self.height )
        for bullet in self.bullets: #ny
            if ((pygame.time.get_ticks() - bullet.timer)/1000) < 1:
                bullet.update(self.width, self.height)
            else:
                self.bullets.remove(bullet)        # TODO: should probably call update on our bullet/bullets here
        # TODO: should probably work out how to remove a bullet when it gets old
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship.py:
        if self.ship:
            self.ship.draw( self.screen )
        # Render all the stars, if any:
        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:
        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the bullet, if any:
        for bullet in self.bullets:
            bullet.draw( self.screen )


    def handle_collisions(self):
        """
        handle_collisions() should check:
            - if our ship.py has crashed into an asteroid (the ship.py gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """
        # TODO: implement collission detection,
        #       using the collission detection methods in all of the shapes
        for asteroid in self.asteroids:
            if asteroid.collide(self.ship):
                print("krock")
                self.running=False

            #for bullet in self.bullets:
             #   asteroid.collide(bullet)
              #  print("bullet")







