from wave_helper import *
import copy
import math
import os.path

def change_file_input():
    """
    this function requires from the user to enter an input (1,2,3,4,5,6)
    and while the input is not one of these numbers it will ask the user
    to enter another input.
    :return: this function returns the right input that the user entered.
    """
    # asking the user to enter an input.
    change_file = input("Enter"
                        "\n1 for reversing"
                        "\n2 for speed acceleration"
                        "\n3 for slowing speed"
                        "\n4 for increasing the volume"
                        "\n5 for decreasing the volume"
                        "\n6 for low pass filter: ")
    while change_file not in ["1", "2", "3", "4", "5", "6"]:
        print("you have entered wrong changing option !")
        change_file = input("Enter"
                            "\n1 for reversing"
                            "\n2 for speed acceleration"
                            "\n3 for slowing speed"
                            "\n4 for increasing the volume"
                            "\n5 for decreasing the volume"
                            "\n6 for low pass filter: ")
    return change_file


def option_input():
    """
    this function requires from the user to enter an input (1,2,3,4) and while
    the input in not one of these numbers it will ask the user to enter
    another input.
    :return: this function returns the right input that the user entered.
    """
    # asking the user to enter an input.
    option = input("Enter"
                   "\n1 for changing the wav file"
                   "\n2 for emerging two wav file"
                   "\n3 for tone composition"
                   "\n4 for exit the program: ")
    while option not in ["1", "2", "3", "4"]:
        print("you have entered a wrong choice !")
        option = input("Enter"
                       "\n1 for changing the wav file"
                       "\n2 for emerging two wav file"
                       "\n3 for tone composition"
                       "\n4 for exit the program: ")
    return option


def file_input():
    """
    this function askes the user to enter the wav file name that he want to
    use for the program, if the name of the file is not founded the function
    askes the user to enter another input until the user enters an appropiate
    input.
    :return: the function returns the correct wav file name.
    """
    file_name = input("enter the wav file name that you want to work with: ")
    while not os.path.exists(file_name):
        print("you have entered non existed wav file name !")
        file_name = input("enter the wav file name that you want "
                          "to work with: ")

    return file_name


def reverse_sound_list(filename):
    """
    this function reverse the required list.
    :param filename: this is the required list to reverse.
    :return: this function returns the required list reversed.
    """
    sound_list = load_wave(filename)[1][::-1]  # reversing the list
    return sound_list


def speed_acceleration(sound_list):
    """
    this function takes the samples in the even indexes from the required list.
    :param sound_list: this is the required list to work with.
    :return: this function returns a modified list.
    """
    for index in range(len(sound_list)):
        if index % 2 == 0:
            # removing the index value from the list
            sound_list = sound_list[:index] + sound_list[index:]
    return sound_list


def slowing_speed(sound_list):
    """
    this function adds to the required list between every two samples in the
    list a new sample that it is the average of the two samples.
    :param sound_list: this is the required list that we will add to it.
    :return: this function returns a modified list.
    """
    new_sound_list = []  # new empty list for saving the values in it
    for index in range(len(sound_list) - 1):
        # adding the original list's values to the helping list (the empty one)
        new_sound_list.append(sound_list[index])
        # taking the average of the samples
        average1 = int((sound_list[index][0] + sound_list[index + 1][0]) / 2)
        average2 = int((sound_list[index][1] + sound_list[index + 1][1]) / 2)
        new_sound_list.append([average1, average2])
    new_sound_list.append(sound_list[-1])
    return new_sound_list


def increasing_volume(sound_list):
    """
    this function multiple the value of the sound list with 1.2, but if the
    valueexceed the number 32767 it will be replaced with it, and if it exceed
    the number -32768 it will be replaced with it.
    :param sound_list: this is the required list to multiple its values.
    :return: this function returns the list modified.
    """
    new_sound_list = []
    for lst in sound_list:
        mtx = []
        x = int(lst[0] * 1.2)
        # checking if both numbers in range or not and adding them to a list
        if x < 0 and x < -32768:
            x = -32768
        elif x > 0 and x > 32767:
            x = 32767
        mtx.append(x)
        y = int(lst[1] * 1.2)
        if y < 0 and y < -32768:
            y = -32768
        elif y > 0 and y > 32767:
            y = 32767
        mtx.append(y)
        new_sound_list.append(mtx)
    return new_sound_list


def decreasing_volume(sound_list):
    """
        this function divides the value of the sound list by 1.2.
        :param sound_list: this is the required list to divide its values.
        :return: this function returns the list modified.
        """
    new_sound_list = []  # new empty list to save the modified list in it
    for lst in sound_list:
        new_sound_list.append([int(lst[0] / 1.2), int(lst[1] / 1.2)])
    return new_sound_list


def filter(sound_list):
    """
    this function filtering the values of the received list, by replacing
    every value with the average of the value in the left and in the right
    and itself.
    :param sound_list: the required list to filter.
    :return: the function returns the filtered list.
    """
    new_sound_list = []  # empty list to add the filtered values to it
    # taking the average of both values in the lists in the bigger one
    avg_sample1 = int((sound_list[0][0] + sound_list[1][0]) / 2)
    avg_sample2 = int((sound_list[0][1] + sound_list[1][1]) / 2)
    new_sound_list.append([avg_sample1, avg_sample2])
    for index in range(1, len(sound_list) - 1):
        avg_sample1 = int(((sound_list[index - 1][0] + sound_list[index][
            0] + sound_list[index + 1][0]) / 3))
        avg_sample2 = int(((sound_list[index - 1][1] + sound_list[index][
            1] + sound_list[index + 1][1]) / 3))
        new_sound_list.append([avg_sample1, avg_sample2])
    # adding the filtered value of the last value in the list
    avg_sample1 = int((sound_list[-1][0] + sound_list[-2][0]) / 2)
    avg_sample2 = int((sound_list[-1][1] + sound_list[-2][1]) / 2)
    new_sound_list.append([avg_sample1, avg_sample2])
    return new_sound_list


def simple_GCD(x, y):
    """
    this function works to find the gcd of two numbers
    :param x: the first number
    :param y: the second number
    :return: the function returns the gcd of both numbers
    """
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


###### Consolidation ######
def list1_longer_list2(sound_list1, sound_list2):
    """
    this function do the consolidation if the first list is longer than the
    second list and the same frame rate.
    :param sound_list1: the first list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    consolidation_list = []
    for i in range(len(sound_list2)):
        avg1 = int((sound_list1[i][0] + sound_list2[i][0]) / 2)
        avg2 = int((sound_list1[i][1] + sound_list2[i][1]) / 2)
        consolidation_list.append([avg1, avg2])
    # this loop to add all the values that have not any counterpart in the
    # other list (by the indexes)
    for i in range(len(sound_list2), len(sound_list1)):
        consolidation_list.append(sound_list1[i])
    return consolidation_list


def list2_longer_list1(sound_list1, sound_list2):
    """
    this function do the consolidation if the second list is longer than
    the first list and the same frame rate.
    :param sound_list1: the first list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    consolidation_list = []
    for i in range(len(sound_list1)):
        avg1 = int((sound_list1[i][0] + sound_list2[i][0]) / 2)
        avg2 = int((sound_list1[i][1] + sound_list2[i][1]) / 2)
        consolidation_list.append([avg1, avg2])
    # this loop to add all the values that have not any counterpart in the
    # other list (by the indexes)
    for i in range(len(sound_list1), len(sound_list2)):
        consolidation_list.append(sound_list2[i])
    return consolidation_list


def list1_equal_list2(sound_list1, sound_list2):
    """
    this function do the consolidation for two list that have the same
    length and the same frame rate.
    :param sound_list1: the first list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    consolidation_list = []
    for i in range(len(sound_list1)):
        avg1 = int((sound_list1[i][0] + sound_list2[i][0]) / 2)
        avg2 = int((sound_list1[i][1] + sound_list2[i][1]) / 2)
        consolidation_list.append([avg1, avg2])
    return consolidation_list


def frame1_bigger_frame2(frame_rate1, sound_list1, frame_rate2, sound_list2):
    """
    this function consolidate the two lists, but the first frame rate is
    bigger than the second frame rate and different length.
    :param frame_rate1: the frame rate for the first list.
    :param sound_list1: the first list.
    :param frame_rate2: the frame rate for the second list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    modified_list = []
    for i in range(0, len(sound_list1), frame_rate1):
        modified_list += sound_list1[i:i + frame_rate2]
    if len(sound_list2) > len(modified_list):
        consolidation_list = list1_longer_list2(sound_list2, modified_list)
    elif len(sound_list2) < len(modified_list):
        consolidation_list = list2_longer_list1(sound_list2, modified_list)
    else:
        consolidation_list = list1_equal_list2(sound_list2, modified_list)
    return consolidation_list


def frame2_bigger_frame1(frame_rate1, sound_list1, frame_rate2, sound_list2):
    """
    this function consolidate the two lists, but the second frame rate is
    bigger than the first frame rate and different length.
    :param frame_rate1: the frame rate for the first list.
    :param sound_list1: the first list.
    :param frame_rate2: the frame rate for the second list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    modified_list = []
    for i in range(0, len(sound_list2), frame_rate2):
        modified_list += sound_list2[i:i + frame_rate1]
    if len(sound_list1) > len(modified_list):
        consolidation_list = list1_longer_list2(sound_list1, modified_list)
    elif len(sound_list1) < len(modified_list):
        consolidation_list = list2_longer_list1(sound_list1, modified_list)
    else:
        consolidation_list = list1_equal_list2(sound_list1, modified_list)
    return consolidation_list


def frames_equal(sound_list1, sound_list2):
    """
    this function consolidate the two lists with the same frame rate,
    but maybe not the same length.
    :param sound_list1: the first list.
    :param sound_list2: the second list.
    :return: this function returns the consolidated list.
    """
    if len(sound_list1) > len(sound_list2):
        consolidation_list = list1_longer_list2(sound_list1, sound_list2)
    elif len(sound_list1) < len(sound_list2):
        consolidation_list = list2_longer_list1(sound_list1, sound_list2)
    else:
        consolidation_list = list1_equal_list2(sound_list1, sound_list2)
    return consolidation_list


def consolidation(frame_rate1, sound_list1, frame_rate2, sound_list2):
    """
    this function do all the consolidation with two lists and two frame rates.
    :param frame_rate1: the first frame rate.
    :param sound_list1: the first list.
    :param frame_rate2: the second frame rate.
    :param sound_list2: the second list.
    :return: this function returns: if the user want to change the file it
    will go to change_file function, and if the user want to save the
    consolidated file it will save it and return 0
    """
    gcd = simple_GCD(frame_rate1, frame_rate2)
    min_frame = min(frame_rate1, frame_rate2)
    frame_rate1 = frame_rate1 // gcd
    frame_rate2 = frame_rate2 // gcd
    if frame_rate1 == frame_rate2:
        consolidation_list = frames_equal(sound_list1, sound_list2)
    elif frame_rate1 > frame_rate2:
        consolidation_list = frame1_bigger_frame2(frame_rate1, sound_list1,
                                                  frame_rate2, sound_list2)
    else:
        consolidation_list = frame2_bigger_frame1(frame_rate1, sound_list1,
                                                  frame_rate2, sound_list2)
    return min_frame, consolidation_list


SAMPLE_RATE = 2000  #magic number of the constant sample rate
MAX_VOLUME = 32767  #magic number for the constant max vloume


######Composite ######


def sample_per_cycle(letter):
    """
    this function takes the frequency f each letter and calculates the
    samples per cycle.
    :param letter: the required letter to take his frequency from the table.
    :return: this function returns the samples per cycle for the letter.
    """
    if letter == "A":
        frequency = 440
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "B":
        frequency = 494
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "C":
        frequency = 523
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "D":
        frequency = 587
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "E":
        frequency = 659
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "F":
        frequency = 698
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle

    elif letter == "G":
        frequency = 784
        samples_per_cycle = SAMPLE_RATE / frequency
        return samples_per_cycle


def read_wordlist_file(filename):
    """
    open the file in the variable filename, and return the words in it
    :param filename: the file that we wanna read the lines from it.
    :return: this function returns a list with all strings in it.
    """
    input_list = []
    contents = open(filename).readlines()
    for line in contents:
        input_list += line.rstrip().split(" ")
    while '' in input_list:
        input_list.remove('')
    return input_list


def samples(j, sample_per_cycle):
    """
    this function calculates the samples for each letter.
    :param j: the index.
    :param sample_per_cycle: the number of samples per cycle.
    :return: the function returns a list
    """
    x = int(MAX_VOLUME * math.sin((math.pi * 2) * (j / sample_per_cycle)))
    return [x, x]


def composition(filename):
    """
    this function gets a text and makes it a sound.
    :param filename: the txt file that we wanna open.
    :return: this function returns: if the user want to change the file it
    will go to change_file function, and if the user want to save the file
    it will save it and return 0
    """
    composite_list=read_wordlist_file(filename)
    sound_list = []
    samples_per_cycle = 0
    for i in range(0, len(composite_list) - 1, 2):
        letter = composite_list[i]
        time = int((int(composite_list[i + 1]) * (1 / 16)) * SAMPLE_RATE)
        samples_per_cycle=sample_per_cycle(letter)
        for j in range(time):
            if letter == "Q":
                sound_list.append([0, 0])
            else:
                x=samples(j,samples_per_cycle)
                sound_list.append(x)

    return transition_menu(2000,sound_list)


######composite######
def changing_file():
    """
    this function askes the user to enter wav file's name, and makes the
    changes that the user wants.
    :return: this function returns: if the user want to change the
    changed file again it will go to change_file function, and if the user
    want to save the changed file.
    it will save it and return 0
    """
    file_name = file_input()
    change_file = change_file_input()
    sound_list = copy.deepcopy(load_wave(file_name)[1])
    if change_file == "1":
        sound_list = reverse_sound_list(file_name)

    elif change_file == "2":
        sound_list = speed_acceleration(load_wave(file_name)[1])

    elif change_file == "3":
        sound_list = slowing_speed(load_wave(file_name)[1])

    elif change_file == "4":
        sound_list = increasing_volume(load_wave(file_name)[1])

    elif change_file == "5":
        sound_list = decreasing_volume(load_wave(file_name)[1])

    elif change_file == "6":
        sound_list = filter(load_wave(file_name)[1])

    return transition_menu(load_wave(file_name)[0],sound_list)


def transition_menu(frame_rate, audio_data):
    """
    this function askes the user if he wants to change the file, or to save it.
    :param frame_rate: the frame rate of the required file to save.
    :param audio_data: the audio list of the required file to save.
    :return: this function returns: if the user want to change the file it
    will go to change_file function, and if the user want to save the file
    it will save it and return 0.
    """
    transition = input("Enter (1) for saving the file or (2) for "
                       "changing the wav file: ")
    while transition not in ["1", "2"]:
        transition = input("Enter (1) for saving the file or (2) for "
                           "changing the wav file: ")
    if transition == "1":
        file_name=input("Enter the name of the file that you wanna save to: ")
        while save_wave(frame_rate, audio_data, file_name) == -1:
            file_name = input("Enter the name of the file that you wanna "
                              "save to: ")
        return 0
    elif transition_menu == "2":
        return changing_file()


def main():
    """
    this function plays all program, by merging all the required functions
    with each others.
    :return: this function returns for the first three options: if the user
    want to change the changed file again it will go to change_file function,
    and if the user want to save the file it will save it and return 0.
    and if the user wanna exit the program without doing anything it will
    return None.
    """
    option = option_input()

    if option == "1":
        return changing_file()

    elif option == "2":
        wav_file1 = input("Enter the first file's name: ")
        wav_file2 = input("Enter the second file's name: ")
        while load_wave(wav_file1) == -1 and load_wave(wav_file2) == -1:
            print("ERROR, you have entered wrong file name !")
            wav_file1 = input("Enter the first file's name: ")
            wav_file2 = input("Enter the second file's name: ")
        frame_rate1=load_wave(wav_file1)[0]
        frame_rate2 = load_wave(wav_file2)[0]
        audio_list1 = load_wave(wav_file1)[1]
        audio_list2 = load_wave(wav_file2)[1]
        return consolidation(frame_rate1,audio_list1,frame_rate2,audio_list2)

    elif option == "3":
        wav_file = input("Enter the composition file's name: ")
        while not os.path.exists(wav_file):
            print("ERROR, you have entered wrong file name !")
            wav_file = input("Enter the composition file's name: ")
        return composition(wav_file)
    elif option=="4":
        return "Exiting the program"

if __name__=="__main__":
    main()