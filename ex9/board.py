U_MESSAGE = "cause the car to move one coordinate up"
D_MESSAGE = "cause the car to move one coordinate down"
L_MESSAGE = "cause the car to move one coordinate to the left"
R_MESSAGE = "cause the car to move one coordinate to the right"


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__block = [["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_","E"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"], ]
        self.target = (3, 7)
        self.current_cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        text = ''
        for row in range(len(self.__block)):
            t = ''
            for column in range(len(self.__block)):
                t += self.__block[row][column] + " "
                if row == 3 and column == 6:
                    t += 'E'
            text += (t + '\n')
        return text

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for row in range(len(self.__block)):
            for column in range(len(self.__block)):
                lst.append((row, column))
                # if row == 3 and column == 6:
                #     lst.append(self.target)
        lst.append((3,7))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value
        # could be
        # [('O','d',"some description"),('R','r',"some description"),
        # ('O','u',"some description")]
        possible_moves_list = []
        for car in self.current_cars:
            name = car.get_name()
            for movekey in car.possible_moves():
                coordinate = car.movement_requirements(movekey)[0]
                description = car.possible_moves()[movekey]
                if coordinate in self.cell_list() and \
                   self.cell_content(coordinate) is None:
                    possible_moves_list.append((name, movekey, description))
        return possible_moves_list

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        row, col = self.target
        return (row, col)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        if coordinate in self.cell_list():
            for car in self.current_cars:
                last_coordinate=car.car_coordinates()[-1]
                if last_coordinate==(3,7):
                    return car.get_name()
            if coordinate == (3, 7):
                pass
            else:
                row, column = coordinate
                if self.__block[row][column] == '_':
                    return None
                else:
                    return self.__block[row][column]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        coordinates_list = car.car_coordinates()
        # if car.get_name() not in "YBOWGR":
        #     return False
        for coordinate in coordinates_list:
            if coordinate not in self.cell_list():
                return False
            if self.cell_content(coordinate) is not None:
                return False
        for i in range(len(self.current_cars)):
            if car.get_name() == self.current_cars[i].get_name():
                return False
        for index in range(car.length):
            row, column = car.car_coordinates()[index]
            self.__block[row][column] = car.get_name()
        self.current_cars.append(car)

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for car in self.current_cars:
            coordinate=car.movement_requirements(movekey)
            x, y = car.location
            if car.get_name()==name and coordinate[0] in self.cell_list():
                row, col = coordinate[0]
                if car.move(movekey) and self.__block[row][col]=='_' or \
                        self.__block[row][col]=='E':
                    self.__block[x][y] = '_'
                    # x1,y1=car.loc
                    self.__block[row][col]=name
                    return True
