from hangman_helper import *


def update_word_pattern(word, pattern, letter):
    """
    this function check if the letter in word and put it in the appropiate
    place in pattern
    :param word: the word that we will play with
    :param pattern: this pattern that we will put the guessed letter in it
    :param letter: the letter that we will check if it in word or not
    :return: the function returns the pattern after the guess process
    """
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                pattern = pattern[:i] + letter + pattern[i + 1:]
    return pattern


thisdict = {}
for i in range(26):#creates a dict with all the alphabet
    thisdict[chr(i + 97)] = 0


def run_single_game(words_list):
    """
    this function runs a single hangman game
    :param words_list this list is the list that contains all the words that
    will randomly played with in the game:
    :return the function returns nothing:
    """
    random_word = get_random_word(words_list)  # get random word from words_list
    wrong_guesses = []
    pattern = '_' * len(random_word)  # make a string with "_" like length of
    # the random word
    default_message = DEFAULT_MSG
    # this loop works if we could not find the word or we override the
    # MAX_ERRORS
    while '_' in pattern and len(wrong_guesses) < MAX_ERRORS:
        display_state(pattern, len(wrong_guesses), wrong_guesses,default_message)
        choice = get_input()
        if choice[0] == HINT:
            filtered_list = filter_words_list(words_list,pattern,wrong_guesses)
            hint = choose_letter(filtered_list, pattern)
            default_message=HINT_MSG+hint
            display_state(pattern,len(wrong_guesses),wrong_guesses,default_message)

        if choice[0]==LETTER:
            # this if checks if the string is longer that 1 and if it is not a
            # lowercase letter
            if (len(choice[1]) != 1) or (choice[1] not in thisdict):
                default_message = NON_VALID_MSG
            elif choice[1] in pattern or choice[1] in wrong_guesses:
                default_message = ALREADY_CHOSEN_MSG + choice[1]
            elif choice[1] in random_word:
                pattern = update_word_pattern(random_word, pattern, choice[1])
                default_message = DEFAULT_MSG
            else:
                wrong_guesses.append(choice[1])
                default_message = DEFAULT_MSG
    if "_" not in pattern:
         default_message = WIN_MSG
         display_state(pattern, len(wrong_guesses), wrong_guesses,default_message, ask_play=True)
    else:
        default_message = LOSS_MSG + random_word
        display_state(pattern, len(wrong_guesses), wrong_guesses,
                       default_message, ask_play=True)


def main():
    """
    this function loads the words from the text file words.txt and put them
    in word_list then it will run the game with this words_list, and while
    the user presses the PLAY AGAIN button it will start a new game
    :return:
    """
    words_list = load_words("words.txt")
    run_single_game(words_list)
    while get_input()[1]:
        run_single_game(words_list)


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    this function filter the words list from the unwanted words in it
    :param words the list of words that we will filter it:
    :param pattern the pattern that the filtered words must be appropiate
    for it:
    :param wrong_guess_lst the list with the wrong guessed letters:
    :return the function returns a filtered list:
    """
    for word in words:
        if len(word)==len(pattern):
            for letter in wrong_guess_lst:
                if letter in word:
                    words.remove(word)
                    break
            else:
                continue
            for index in range(len(pattern)):
                if pattern[index]!='_' and (pattern[index]!=word[index]):
                    words.remove(word)
                elif word.count(pattern[index])!=pattern.count(pattern[index]):
                    words.remove(word)
        else:
            words.remove(word)
    return words


def choose_letter(words, pattern):
    """
    this function finds the letter that he appears the most in the list (words)
    :param words list of words that we will search in:
    :param pattern the pattern of the words in the list that we will serch in:
    :return the function returns the letter that he appears the most in the list:
    """
    for word in words:
        if len(word) == len(pattern):
            for w in word:
                thisdict[w] += 1
    inverse = [(value, key) for key, value in thisdict.items()]
    return max(inverse)[1]


thisdict['g']+=2
thisdict['c']+=1
lst=[]
for i in thisdict:
    lst.append((i,thisdict[i]))


maximum=lst[0][1]
char=lst[0][0]
for i in range(1,len(lst)):
    if lst[i][1]>maximum:
        maximum=lst[i][1]
        char=lst[i][0]



if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()

