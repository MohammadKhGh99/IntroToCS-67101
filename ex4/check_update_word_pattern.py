from hangman import update_word_pattern


def check():
    if update_word_pattern('apple','___l_','1')=='___l_':
        if update_word_pattern('mohammad','___a__a_','m')=='m__amma_':
            if update_word_pattern('science','_c___c_','c')=='_c___c_':
                if update_word_pattern('orange','__ang_','o')=='__ang_':
                    print("Function "+"update_word_pattern"+" test success")
                    return True
                else:
                    print("Function " + "update_word_pattern" + " test fail")
                    return False
            else:
                print("Function " + "update_word_pattern" + " test fail")
                return False
        print("Function " + "update_word_pattern" + " test fail")
        return False
    else:
        print("Function " + "update_word_pattern" + " test fail")
        return False

if __name__=="__main__":
    check()