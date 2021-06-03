from math import *

SCORE_3=20
SCORE_2=50
SCORE_1=100


class Asteroid:

    def __init__(self, xcoordinate, xspeed, ycoordinate, yspeed,size):
        self.__xcoordinate = xcoordinate
        self.__xspeed = xspeed
        self.__ycoordinate = ycoordinate
        self.__yspeed = yspeed
        self.__size = size

    # set and get methods for the class
    def get_xcoordinate(self):
        return self.__xcoordinate

    def set_xcoordinate(self, x):
        self.__xcoordinate = x

    def get_ycoordinate(self):
        return self.__ycoordinate

    def set_ycoordinate(self, y):
        self.__ycoordinate = y

    def get_xspeed(self):
        return self.__xspeed

    def set_xspeed(self, x):
        self.__xspeed = x

    def get_yspeed(self):
        return self.__yspeed

    def set_yspeed(self, y):
        self.__yspeed = y

    def get_size(self):
        return self.__size

    def set_size(self, x):
        self.__size = x

    def get_radius(self):
        radius = (self.__size * 10) - 5
        return radius

    def has_intersection(self, obj):
        """
        this method checks if the asteroid collide with another object
        :param obj: the chosen object
        :return: True if there is collision and False if not
        """
        delta_x = obj.get_xcoordinate() - self.get_xcoordinate()
        delta_y = obj.get_ycoordinate() - self.get_ycoordinate()
        distance = sqrt(pow(delta_x, 2) + pow(delta_y, 2))
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_score(self):
        """
        this method returns the score that given for this asteroid when it
        destroyed.
        :return: returns None
        """
        if self.get_size()==1:
            return 100
        elif self.get_size()==2:
            return 50
        elif self.get_size()==3:
            return 20
