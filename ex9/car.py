U_MESSAGE = "cause the car to move one coordinate up"
D_MESSAGE = "cause the car to move one coordinate down"
L_MESSAGE = "cause the car to move one coordinate to the left"
R_MESSAGE = "cause the car to move one coordinate to the right"
OUT_OF_GAME = "Look Out You Are Getting Out Of The Game !!!"
WRONG_DIRECTION = "You Have Entered A Wrong Directions !!!"
INVALID_DIRECTION = "You Have Entered Invalid Direction !!!"


class Car:
    """
    Add class description here
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row,
        col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.length = length
        self.__name = name
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        x, y = self.location
        lst = [(x, y)]
        if self.orientation == 0:
            for i in range(self.length - 1):
                x+=1
                lst.append((x, y))
        else:
            for i in range(self.length - 1):
                y+=1
                lst.append((x, y))

        return lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        if self.orientation == 0:
            permitted_directions = {'u': U_MESSAGE,'d': D_MESSAGE}
        else:
            permitted_directions = {'r': R_MESSAGE,'l': L_MESSAGE}
        return permitted_directions

    ##############################################################################
    def vertical_move_requirements(self, movekey):
        x, y = self.location
        x1 = (x + self.length - 1)
        if movekey == "u":
            return [(x - 1, y)]
        elif movekey == 'd':
            return [(x1 + 1, y)]
        else:
            print(WRONG_DIRECTION)
            return []

    def horizontal_move_requirements(self, movekey):
        x, y = self.location
        y1 = (y + self.length - 1)
        if movekey=='r':
            return [(x, y1 + 1)]
        elif movekey=='l':
            return [(x, y - 1)]
        else:
            print(WRONG_DIRECTION)
            return []

    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        if movekey in 'udrl':
            if self.orientation == 0:
                coordinate=self.vertical_move_requirements(movekey)
                return coordinate
            else:
                coordinate=self.horizontal_move_requirements(movekey)
                return coordinate
        else:
            print(INVALID_DIRECTION)
            return []

    ##############################################################################
    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        x, y = self.location
        if movekey not in 'udrl':
            print(INVALID_DIRECTION)
            return False
        elif self.orientation == 0:
            if movekey=='u':
                self.location=(x-1,y)
                return True
            elif movekey=='d':
                self.location=(x+1,y)
                return True
            else:
                print(WRONG_DIRECTION)
                return False
        elif self.orientation == 1:
            if movekey=='r':
                self.location=(x,y+1)
                return True
            elif movekey=='l':
                self.location=(x,y-1)
                return True
            else:
                print(WRONG_DIRECTION)
                return False
        else:
            return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.__name
