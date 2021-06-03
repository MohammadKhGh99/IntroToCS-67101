def largest_and_smallest(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    min =a
    if b<min:
        min=b
    if c<min:
        min=c
    return max,min