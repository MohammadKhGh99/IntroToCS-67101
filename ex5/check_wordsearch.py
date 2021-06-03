from wordsearch import *


def check():
    flag=True
    if r_l_u_d_search('apple',read_matrix_file("mat.txt"),"r")!=1:
        flag=False
    if r_l_u_d_search('dog',read_matrix_file("mat.txt"),'l')!=1:
        flag=False
    if r_l_u_d_search('toe',read_matrix_file("mat.txt"),'u')!=1:
        flag=False
    if r_l_u_d_search('poeT',read_matrix_file("mat.txt"),'d')!=1:
        flag=False

    if flag==True:
        return True
    else:
        return False

if __name__=="__main__":
    check()