def calculate_mathematical_expression(x1,x2,s):
    if(s=="+"):
        return x1+x2
    elif(s=="-"):
        return x1-x2
    elif(s=="*"):
        return x1*x2
    elif(s=="/"):
        if x2!=0 :
            return float(x1/x2)
        else:
                return None
    else:
        return None

def calculate_from_string(exp):
    if exp=="":
        return None
    else:
        a1,b,a2=exp.split(" ")
        return calculate_mathematical_expression(float(a1),float(a2),b)