import math
def shape_area():
    s=input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if s=="1":
        r=float(input())
        return math.pi*(r**2)
    elif s=="2":
        a=float(input())
        b=float(input())
        return a*b
    elif s=="3":
        a=float(input())
        return ((3**0.5)*a**2)/4
    else:
        return None