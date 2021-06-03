from screen import Screen
import sys
from ship import Ship
from random import randint
from math import *
from torpedo import Torpedo
from asteroid import Asteroid

DEFAULT_ASTEROIDS_NUM = 5
SHIP_TITLE = "Asteroid_Ship Intersection !"
TORPEDO_TITLE = "Asteroid_Torpedo Intersection !"
SHIP_MESSAGE = "Look Out! You Have Been Hit By An Asteroid!"
NO_ASTEROIDS_TITLE = "You Have Won!"
NO_ASTEROIDS_LEFT = "Woo Hoo! You Have Destroyed All The Asteroids"
NO_LIVES_TITLE = "Game Over!"
NO_LIVES = "Oh Oh You Have Failed, No Lives Left!"
QUIT_TITLE = "Exit"
QUIT = "You Are Quitting The Game!"


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        x = randint(self.__screen_min_x, self.__screen_max_x + 1)
        y = randint(self.__screen_min_y, self.__screen_max_y + 1)
        self.__ship = Ship(x, y)
        # initializing the asteroids in the screen
        self.__asteroids_list = []
        for i in range(asteroids_amount):
            xcoordinate = randint(self.__screen_min_x, self.__screen_max_x + 1)
            ycoordinate = randint(self.__screen_min_y, self.__screen_max_y + 1)
            xspeed = randint(1, 5)
            yspeed = randint(1, 5)
            asteroid = Asteroid(xcoordinate, xspeed, ycoordinate, yspeed, 3)
            self.__asteroids_list.append(asteroid)
            self.__screen.register_asteroid(asteroid, asteroid.get_size())
            self.__screen.draw_asteroid(asteroid, xcoordinate, ycoordinate)
        # initializing the amount of the torpedos in the screen (zero)
        self.__torpedos_list = []
        # initializing the score number
        self.__score = 0
        # initializing the amount of the special torpedos in the screen (zero)
        self.__special_torpedos = []

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    ##############################################################################

    def move(self, obj):
        """
        this method moves the obj by a helping equation
        :param obj: the chosen object to move
        :return: the method returns None
        """
        old_xcoordinate = obj.get_xcoordinate()
        old_ycoordinate = obj.get_ycoordinate()
        xspeed = obj.get_xspeed()
        yspeed = obj.get_yspeed()
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_xcoordinate = (xspeed + old_xcoordinate - self.__screen_min_x) % \
                          delta_x + self.__screen_min_x
        new_ycoordinate = (yspeed + old_ycoordinate - self.__screen_min_y) % \
                          delta_y + self.__screen_min_y
        # giving the obj the new x and y coordinates.
        obj.set_xcoordinate(new_xcoordinate)
        obj.set_ycoordinate(new_ycoordinate)

    def change_direction(self, ship):
        """
        this method lets the ship to rotate when the left or right button
        pressed
        :param ship: the chosen ship to rotate
        :return: the method returns None
        """
        direction = ship.get_direction()
        if self.__screen.is_left_pressed():
            direction += 7
            ship.set_direction(direction)
        elif self.__screen.is_right_pressed():
            direction -= 7
            ship.set_direction(direction)

    def acceleration(self, ship):
        """
        this method lets the ship accelerate by pressing the up button.
        :param ship: the chosen ship to accelerate
        :return: the method returns None
        """
        current_xspeed = ship.get_xspeed()
        current_yspeed = ship.get_yspeed()
        direction_in_radian = radians(ship.get_direction())
        if self.__screen.is_up_pressed():
            new_xspeed = current_xspeed + cos(direction_in_radian)
            new_yspeed = current_yspeed + sin(direction_in_radian)
            ship.set_xspeed(new_xspeed)
            ship.set_yspeed(new_yspeed)

    def ship_movement(self, ship):
        """
        thia method responsible of the movement of the ship, acceleration,
        rotation
        :param ship: the chosen ship to move
        :return: the method returns None
        """
        self.move(ship)
        self.change_direction(ship)
        self.acceleration(ship)
        x = self.__ship.get_xcoordinate()
        y = self.__ship.get_ycoordinate()
        d = self.__ship.get_direction()
        self.__screen.draw_ship(x, y, d)
        for asteroid in self.__asteroids_list:
            if asteroid.has_intersection(ship):
                self.__screen.show_message(SHIP_TITLE, SHIP_MESSAGE)
                self.__screen.remove_life()
                life = self.__ship.get_life()
                life -= 1
                self.__ship.set_life(life)
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids_list.remove(asteroid)

    def asteroids_movement(self):
        """
        this method responsible of the movement of the asteroids
        :return:  the method returns None
        """
        for asteroid in self.__asteroids_list:
            self.move(asteroid)
            x = asteroid.get_xcoordinate()
            y = asteroid.get_ycoordinate()
            self.__screen.draw_asteroid(asteroid, x, y)

    def shooting(self):
        """
        this method makes the ship shooting torpedo by pressing on space
        button.
        :return: the method returns None
        """
        x, y = self.__ship.get_xcoordinate(), self.__ship.get_ycoordinate()
        current_xspeed = self.__ship.get_xspeed()
        current_yspeed = self.__ship.get_yspeed()
        direction = self.__ship.get_direction()
        new_xspeed = current_xspeed + 2 * cos(radians(direction))
        new_yspeed = current_yspeed + 2 * sin(radians(direction))
        if self.__screen.is_space_pressed():
            torpedo = Torpedo(x, new_xspeed, y, new_yspeed, direction)
            if torpedo not in self.__torpedos_list:
                if len(self.__torpedos_list) != 10:
                    self.__torpedos_list.append(torpedo)
                    self.__screen.register_torpedo(torpedo)
                    self.__screen.draw_torpedo(torpedo, x, y, direction)

    def torpedo_movement(self):
        """
        this method responsible of the movement of the torpedos
        :return: the method returns None
        """
        for torpedo in self.__torpedos_list:
            self.move(torpedo)
            x = torpedo.get_xcoordinate()
            y = torpedo.get_ycoordinate()
            self.__screen.draw_torpedo(torpedo, x, y, torpedo.get_direction())
            life = torpedo.get_life()
            life += 1
            torpedo.set_life(life)
            if torpedo.get_life() == 200:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedos_list.remove(torpedo)
            for asteroid in self.__asteroids_list:
                if asteroid.has_intersection(torpedo):
                    self.__score += asteroid.get_score()
                    self.__screen.set_score(self.__score)
                    self.after_blowing_asteroid(asteroid, torpedo)

    def blowing_1_asteroid(self, asteroid, torpedo):
        """
        this method works on what happens when a torpedo hit an asteroid
        that his size is 1
        :param asteroid: the asteroid
        :param torpedo: the torpedo
        :return: the method returns None
        """
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids_list.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.__torpedos_list.remove(torpedo)

    def blowing_2_3_asteroid(self, asteroid, torpedo):
        """
        this method responsible of what happens when the torpedo hit an
        asteroid that his ize is 2 or 3
        :param asteroid: the asteroid
        :param torpedo: the torpedo
        :return: the method returns None
        """
        x = asteroid.get_xcoordinate()
        y = asteroid.get_ycoordinate()
        size = asteroid.get_size() - 1
        new_xspeed1 = self.new_asteroids_speed(asteroid, torpedo, 1)[0]
        new_yspeed1 = self.new_asteroids_speed(asteroid, torpedo, 1)[1]
        new_xspeed2 = \
            self.new_asteroids_speed(asteroid, torpedo, -1)[0]
        new_yspeed2 = \
            self.new_asteroids_speed(asteroid, torpedo, -1)[1]
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids_list.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.__torpedos_list.remove(torpedo)
        asteroid1 = Asteroid(x, new_xspeed1, y, new_yspeed1, size)
        asteroid2 = Asteroid(x, new_xspeed2, y, new_yspeed2, size)
        self.__screen.register_asteroid(asteroid1, size)
        self.__screen.register_asteroid(asteroid2, size)
        self.__asteroids_list.append(asteroid1)
        self.__asteroids_list.append(asteroid2)

    def after_blowing_asteroid(self, asteroid, torpedo):
        """
        this method collect everything that happens when a torpedo hit an
        asteroid.
        :param asteroid: the asteroid
        :param torpedo: the torpedo
        :return: the method returns None
        """
        if asteroid.get_size() == 3 or asteroid.get_size() == 2:
            self.blowing_2_3_asteroid(asteroid, torpedo)
        else:
            self.blowing_1_asteroid(asteroid, torpedo)

    def new_asteroids_speed(self, asteroid, torpedo, r):
        """
        this method calculates the new speeds of the asteroids that blew
        from the destroyed asteroid
        :param asteroid: the destroyed asteroid
        :param torpedo: the torpedo
        :param r: 1 for the positive speed and -1 for the negative speed
        :return: this method returns the new speeds of the new asteroids
        """
        if r == 1:
            current_xspeed = asteroid.get_xspeed()
            current_yspeed = asteroid.get_yspeed()
        else:
            current_xspeed = -1 * asteroid.get_xspeed()
            current_yspeed = -1 * asteroid.get_yspeed()
        new_xspeed = (torpedo.get_xspeed() + current_xspeed) \
                     / sqrt(current_xspeed ** 2 + current_yspeed ** 2)
        new_yspeed = (torpedo.get_yspeed() + current_yspeed) \
                     / sqrt(current_xspeed ** 2 + current_yspeed ** 2)

        return new_xspeed, new_yspeed

    def end_game(self):
        """
        this method handle when the game ends
        :return:  the method returns None
        """
        if self.__asteroids_list == []:
            self.__screen.show_message(NO_ASTEROIDS_TITLE, NO_ASTEROIDS_LEFT)
            self.__screen.end_game()
            sys.exit()
        if self.__ship.get_life() == 0:
            self.__screen.show_message(NO_LIVES_TITLE, NO_LIVES)
            self.__screen.end_game()
            sys.exit()
        if self.__screen.should_end():
            self.__screen.show_message(QUIT_TITLE, QUIT)
            self.__screen.end_game()
            sys.exit()

    def teleport(self):
        """
        this method responsible of the teleport action
        :return:  the method returns None
        """
        if self.__screen.is_teleport_pressed():
            x = randint(self.__screen_min_x, self.__screen_max_x + 1)
            y = randint(self.__screen_min_y, self.__screen_max_y + 1)
            self.__ship.set_xcoordinate(x)
            self.__ship.set_ycoordinate(y)
            flag = False
            for asteroid in self.__asteroids_list:
                if asteroid.has_intersection(self.__ship):
                    flag = True
            if not flag:
                self.ship_movement(self.__ship)

    def special_torpedo(self):
        """
        this method is like shooting method, but this makes the ship shoot
        special torpedos
        :return:  the method returns None
        """
        x, y = self.__ship.get_xcoordinate(), self.__ship.get_ycoordinate()
        current_xspeed = self.__ship.get_xspeed()
        current_yspeed = self.__ship.get_yspeed()
        direction = self.__ship.get_direction()
        new_xspeed = current_xspeed + 2 * cos(radians(direction))
        new_yspeed = current_yspeed + 2 * sin(radians(direction))
        if self.__screen.is_special_pressed():
            special_torpedo = Torpedo(x, new_xspeed, y, new_yspeed, direction)
            if special_torpedo not in self.__special_torpedos:
                if len(self.__special_torpedos) != 5:
                    self.__special_torpedos.append(special_torpedo)
                    self.__screen.register_torpedo(special_torpedo)
                    self.__screen.draw_torpedo(special_torpedo, x, y,
                                               direction)

    def special_blowing(self, asteroid, torpedo):
        """
        this method makes the special blowing of the special torpedo
        :param asteroid: the asteroid
        :param torpedo: the torpedo
        :return:  the method returns None
        """
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids_list.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.__special_torpedos.remove(torpedo)

    def special_movement(self):
        """
        this method is responsible of the special torpedo action
        :return:  the method returns None
        """
        self.special_torpedo()
        for special_torpedo in self.__special_torpedos:
            self.move(special_torpedo)
            x = special_torpedo.get_xcoordinate()
            y = special_torpedo.get_ycoordinate()
            direction = special_torpedo.get_direction()
            self.__screen.draw_torpedo(special_torpedo, x, y, direction)
            life = special_torpedo.get_life()
            life += 1
            specia l_torpedo.set_life(life)
            if special_torpedo.get_life() == 150:
                self.__screen.unregister_torpedo(special_torpedo)
                self.__special_torpedos.remove(special_torpedo)
            for asteroid in self.__asteroids_list:
                if asteroid.has_intersection(special_torpedo):
                    self.__score += asteroid.get_score()
                    self.__screen.set_score(self.__score)
                    self.special_blowing(asteroid, special_torpedo)

    def _game_loop(self):
        # Your code goes here
        self.ship_movement(self.__ship)
        self.asteroids_movement()
        self.shooting()
        self.torpedo_movement()
        self.end_game()
        self.teleport()
        self.special_movement()

def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
