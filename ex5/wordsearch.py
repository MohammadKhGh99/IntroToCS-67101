# list of the directions
DIRECTIONS = ["u", "d", "r", "l", "w", "x", "y", "z"]


def check_input_args(args):
    """
    this functions checks if the inputs are false
    :param args: the list of the inputs
    :return: this function returns an adequate message for the false input
    """
    if len(args) != 4:  # checks if the number of the inputs is 4 or not
        return "you have entered wrong number of parameters"
    elif ("word_file.txt" and "matrix_file.txt" not in args) or \
            "word_file.txt" not in args:
        return "there is no words file"
    elif "matrix_file.txt" not in args:
        return "there is no matrix file"
    else:
        for d in args[3]:
            # checks if the entered directions are valid or not
            if d not in DIRECTIONS:
                return "you have entered wrong direction"


def read_wordlist_file(filename):
    """
    this function opens a file and puts all the words in it, in a list
    :param filename: this is the file that we will take the words from it
    and put them in a list
    :return: this function returns a list with all the words in the file
    """
    words = []  # empty list to add the modified words to it
    words_file = open(filename)
    for word in words_file:
        words.append(word.rstrip())  # removing the "\n" from each word
    return words


def read_matrix_file(filename):
    matrix = []  # empty matrix to add all the mat.txt items in it
    matrix_file = open(filename)
    for line in matrix_file:
        # deleting the '\n' from each list in the matrix
        matrix.append(line.rstrip().split(","))
    return matrix


def reverse_matrix_for_left_search(matrix):
    """
    this function reverse each list in the matrix
    :param matrix: the matrix that we want to reverse
    :return: this function return the reversed matrix
    """
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


def replace_matrix_columns_with_rows(matrix):
    """
    this function replace the columns of the matrix with its rows
    :param matrix: the matrix that we want to replace its columns
    :return: this function returns the new matrix
    """
    new_matrix = []  # empty matrix to add the new rows(lists) to it

    for row in range(len(matrix[0])):
        mtx = []
        for column in range(len(matrix)):
            mtx.append(matrix[column][row])
        new_matrix.append(list(mtx))
    return new_matrix


def r_l_u_d_search(word, matrix, direction):
    """
    this function check how much the word appeared at the right or left or
    up or down directions
    :param word: the word that we want to check
    :param matrix: the matrix that we will search in it
    :param direction: the char one of the directions('u','d','r','l')
    :return: this function returns how much the word appeared in the
    adequate direction
    """
    counter = 0  # defining a counter
    if direction == 'l':
        matrix = reverse_matrix_for_left_search(matrix)
    elif direction == 'u':
        new_matrix = replace_matrix_columns_with_rows(matrix)
        matrix = reverse_matrix_for_left_search(new_matrix)
    elif direction == 'd':
        matrix = replace_matrix_columns_with_rows(matrix)
    for row in range(len(matrix)):
        if len(matrix[row]) >= len(word):
            for index in range((len(matrix[row]) - len(word)) + 1):
                if matrix[row][index] == word[0]:
                    x = matrix[row][index]
                    for index_word in range(1, len(word)):
                        x += matrix[row][index_word + index]
                    if x == word:
                        counter += 1

    return counter


def w_x_y_z_search(word, matrix, direction):
    """
    this function check how much the word appeared at the right_up or
    left_up or right_down or left_down directions
    :param word: the word that we want to check
    :param matrix: the matrix that we will search in it
    :param direction: the char one of the directions('w','z','y','x')
    :return: this function returns how much the word appeared in the
    adequate direction
    """
    counter = 0
    if direction == 'x':
        matrix = reverse_matrix_for_left_search(matrix[::-1])
    elif direction == 'z':
        matrix = reverse_matrix_for_left_search(matrix)
    elif direction == 'w':
        matrix = matrix[::-1]
    for row in range(len(matrix) - len(word) + 1):
        if len(matrix[row]) >= len(word):
            for index in range((len(matrix[row]) - len(word)) + 1):
                if matrix[row][index] == word[0]:
                    x = matrix[row][index]
                    for index_word in range(1, len(word)):
                        x += matrix[row + index_word][index + index_word]
                        print(x)
                    if x == word:
                        counter += 1
    return counter


def find_words_in_matrix(word_list, matrix, directions):
    """
    this function checks how much the words in word_list appears in all
    directions in directions parameter
    :param word_list: the list with words
    :param matrix: the matrix that we want to search in it
    :param directions: the string that contains the directions that we want
    to search with
    :return: this function returns list with tuples
    """
    words_and_counters_list=[]
    thisdict = {}
    x = directions[0]
    for i in range(1, len(directions)):
        if directions[i] == x:
            directions = directions[:i] + directions[i + 1:]
        x = directions[i]
    for word in word_list:
        thisdict[word] = 0
    for word in word_list:
        for d in directions:
            if d == 'r' or 'l' or 'u' or 'd':
                thisdict[word] += r_l_u_d_search(word, matrix, d)
            elif d == 'y' or 'x' or 'w' or 'z':
                thisdict[word] += w_x_y_z_search(word, matrix, d)

    words_and_counters_list = list(thisdict.items())
    for index in range(len(words_and_counters_list)):
        if words_and_counters_list[index][1]==0:
            words_and_counters_list=words_and_counters_list[
                                    :index]+words_and_counters_list[index+1:]
    return words_and_counters_list


def write_output_file(results, output_filename):
    f = open(output_filename,'w')
    for index in range(len(results)):
        f.write(results[index])

def main():
    word_list=read_wordlist_file("word_list.txt")
    matrix=read_matrix_file("mat.txt")
    directions="uxyw"
    results=find_words_in_matrix(word_list,matrix,directions)
    write_output_file(results,"output.txt")

# if __name__=="__main__":
#     main()