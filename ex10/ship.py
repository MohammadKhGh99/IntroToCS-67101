class Ship:

    def __init__(self, xcoordinate, ycoordinate):
        self.__xcoordinate = xcoordinate
        self.__xspeed = 0
        self.__ycoordinate = ycoordinate
        self.__yspeed = 0
        self.__direction = 0
        self.__radius=1
        self.__life=3
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

    def get_life(self):
        return self.__life

    def set_life(self,life):
        self.__life=life
