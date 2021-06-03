class Torpedo:

    def __init__(self, xcoordinate, xspeed, ycoordinate, yspeed, direction):
        self.__xcoordinate = xcoordinate
        self.__xspeed = xspeed
        self.__ycoordinate = ycoordinate
        self.__yspeed = yspeed
        self.__direction = direction
        self.__radius = 4
        self.__life=0

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

    def get_direction(self):
        return self.__direction

    def set_direction(self, x):
        self.__direction = x

    def get_radius(self):
        return self.__radius

    def set_radius(self,radius):
        self.__radius=radius

    def get_life(self):
        return self.__life

    def set_life(self,life):
        self.__life=life
