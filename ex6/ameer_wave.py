from wave_helper import *


def option_input():
    option = input("enter \n1 for changing the wave file.\n2 for for emerging two files."
                   "\n3 for tone composition.\n4 exit from the program.")
    while option not in ["1", "2", "3", "4"]:
        print("you have entered invalid number!")
        option = option_input()
    return option


def change_file_input():
    change_file = "enter\n1for reverse\n2 for speed acceleration\n" \
                  "2 for slowing speed\n4 for increasing volume\n" \
                  "5 for decreasing volume\n6 for low pass filter"
    while change_file not in ["1", "2", "3", "4", "5", "6"]:
        print("you have entered invalid number!")
        change_file = change_file_input()
    return change_file


# option = option_input()
#
#
#
#
# if option == "1":
#     file_name = input("enter files name: ")
#     change_file = change_file_input()
#
# elif option == "2":
#     wav_file_1 = "enter the name of the first file: "
#     wav_file_2 = "enter the name of the second file: "
#
# elif option == "3":
#     composition_file = "enter composition_file name: "


def reverse_volume(file_name):
    data_list = load_wave(file_name)[1]
    data_list[:] = data_list[::-1]
    return data_list


def speed_acceleration(data_list):
    lst = []
    for i in range(0, len(data_list), 2):
        lst.append(data_list[i])
    return lst


# print(speed_acceleration([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

def slow_speed(data_list):
    new_list = []
    for i in range(len(data_list)-1):
        new_list.append(data_list[i])
        ameer = int((data_list[i][0] + data_list[i+1][0])/2)
        mos = int((data_list[i][1] + data_list[i+1][1])/2)
        new_list.append([ameer, mos])
    new_list.append(data_list[-1])
    return new_list
# print(slow_speed([[10,10],[20,30],[30,50],[40,60]]))