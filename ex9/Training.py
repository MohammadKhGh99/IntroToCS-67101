class Student:
    def __init__(self,name,Student_list_of_grades):
        self.__name=name
        self.__Student_list_of_grades=Student_list_of_grades
    def get_grade_avg(self):
        return (sum(self.__Student_list_of_grades)/len(self.__Student_list_of_grades))
    def get_name(self):
        return self.__name

class ClassRoom:
    def __init__(self, Students):
        self.__Students = Students
        self.__ls = list()
        for student in self.__Students:
            self.__ls.append((student.get_name(), student.get_grade_avg()))
    def __str__(self):
        return str(self.__ls)

yossi=Student("Yossi",[97.5,87,60])
lital=Student("Lital",[85,96,100])
students=[yossi,lital]
classRoom=ClassRoom(students)
print (classRoom)


# class Bicycle:
#     WHEELS = 2
#
#     def __init__(self, c,Students, color="yellow"):
#         self.__Students=Students
#         self.__ls=list()
#         for student in self.__Students:
#             self.__ls.append(tuple(student.get_name(),student.get_grade_avg))
#
#     def __str__(self):
#         return
#


        # self.__color = color
        # self.abs = c
        # self.__block = [["_", "_", "_", "_", "_", "_", "_"],
        #                 ["_", "_", "_", "_", "_", "_", "_"],
        #                 ["_", "_", "_", "_", "_", "_", "_"],
        #                 ["_", "_", "_", "_", "_", "_", "_", "E"],
        #                 ["_", "_", "_", "_", "_", "_", "_"],
        #                 ["_", "_", "_", "_", "_", "_", "_"],
        #                 ["_", "_", "_", "_", "_", "_", "_"], ]

    # def __str__(self):
    #     """
    #     This function is called when a board object is to be printed.
    #     :return: A string of the current status of the board
    #     """
    #     The game may assume this function returns a reasonable representation
    #     of the board for printing, but may not assume details about it.
        # text = ''
        # for row in range(len(self.__block)):
        #     t = ''
        #     for column in range(len(self.__block)):
        #         t += self.__block[row][column] + " "
        #         if row == 3 and column == 6:
        #             t += 'E'
        #     text += (t + '\n')
        # return text


    # def __str__(self):
    #     return "(the color: " + self.__color + ", the c: " + str(self.abs) + ")"
    #
    # def get_color(self):
    #     return self.__color
    #
    # def set_color(self, color):
    #     self.__color = color
    #     self.__init__(2)
    #
    # def sum_two_numbers(self, a, b):
    #     return a + b


# bicycle1 = Bicycle("blue")
# bicycle2=Bicycle(4)
# bicycle2.set_color("blue")
# bicycle1.WHEELS=4


# print ("hsbfyshbdfkz")

# print (bicycle2)
# print (bicycle1.sum_two_numbers(2,1))
# print (bicycle2.get_color())
# print (bicycle1.get_color())

# b.set_color("blue")

# print (b.get_color())
