import rosegraphics as rg


def jump_to(turtle, x, y):
    turtle.pen_up()
    turtle.go_to(rg.Point(x, y))
    turtle.set_heading(0)
    turtle.pen_down()

def draw_chimmney(turtle):
    jump_to (turtle, 50, 90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)




def draw_box(turtle):
    jump_to(turtle, -80, -160)
    for k in range(4):
        turtle.forward(160)
        turtle.left(90)
def draw_door(turtle):
    jump_to(turtle, -25, -160)
    for k in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
def draw_roof(turtle):
    jump_to(turtle, -100, 0)
    for k in range(3):
        turtle.forward(200)
        turtle.left(120)

def main():
    print("build a mansion")
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("orange", 5)
    while True:
        selection = input("selection: ")
        if selection == "1":
            draw_chimmney(turtle)
        if selection =="2":
            draw_box (turtle)
        if selection=="4":
            draw_door(turtle)
        if selection== "3":
            draw_roof(turtle)
        if selection == "r":
            turtle.pen = rg.Pen("red", 5)

        if selection == "o":
            turtle.pen = rg.Pen("orange", 5)
        if selection == "g":
            turtle.pen = rg.Pen("green", 5)

        if selection == "":
            break


main()
