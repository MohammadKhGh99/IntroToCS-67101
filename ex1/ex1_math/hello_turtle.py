import turtle
def draw_petal():
    """this function draws a petal"""
    turtle.circle(100,90)
    turtle.left(90)
    turtle.circle(100,90)

def draw_flower():
    """this function draws a flower with four petals"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)

def draw_flower_advance():
    """this function works like draw_flower in addition to prepare the pen
    to draw the other flower """
    draw_flower()
    turtle.right(90)
    turtle.penup()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.pendown()

def draw_flower_bed():
    """this function draws flowers' garden includes 3 flowers"""
    turtle.penup()
    turtle.forward(200)
    turtle.left(180)
    turtle.pendown()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done()