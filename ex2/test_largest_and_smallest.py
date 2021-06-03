import largest_and_smallest
def test4():
    if (largest_and_smallest.largest_and_smallest(10,1,5) ==(10,1) \
        and largest_and_smallest.largest_and_smallest(22,25,23)==(25,22) \
        and largest_and_smallest.largest_and_smallest(16,15,40)==(40,15) \
        and largest_and_smallest.largest_and_smallest(2,5,2)==(5,2)\
        and largest_and_smallest.largest_and_smallest(25,12,3)==(12,25)):
        return True,("Function 4 test success")
    else:
        return False,("Function 4 test fail")

if __name__=="__main__":
    print(test4())