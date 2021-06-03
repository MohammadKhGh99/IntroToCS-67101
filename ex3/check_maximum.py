from ex3 import maximum

def check_maximum_function():
    if maximum([1,1,1])==1:
        print("Test 0 OK")
    else:
        print("Test 0 FAIL")
    if maximum([-1,4,1])==4:
        print("Test 1 OK")
    else:
        print("Test 0 FAIL")
    if maximum([2,4,8])==8:
        print("Test 2 OK")
    else:
        print("Test 0 FAIL")
    if maximum([19,4,88])==88:
        print("Test 3 FAIL")
    else:
        print("Test 0 FAIL")


if __name__ == "__main__":
    check_maximum_function()