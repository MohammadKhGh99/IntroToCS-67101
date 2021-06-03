def quadratic_equation(a,b,c):
    if (b**2-4*a*c)>0:
        return (-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)
    elif (b**2-4*a*c)==0:
        return -b/(2*a),None
    else:
        return None,None

def quadratic_equation_user_input():
    quad=input("Insert coefficients a, b, and c: ")
    a,b,c=quad.split(" ")
    a=float(a)
    b=float(b)
    c=float(c)
    if b**2-4*a*c>0:
        x,y=quadratic_equation(a,b,c)
        print("The equation has 2 solutions:",x,"and",y)
    elif b**2-4*a*c==0:
        print("The equation has 1 solution:",(-b/(2*a)))
    else:
        print("The equation has no solutions")