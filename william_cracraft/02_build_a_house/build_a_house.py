import rosegraphics as rg

def main():
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("blue", 3)
    turtle.speed = 20

    while True:
        selection = input("select an option:")
        if selection == "1":
            draw_chimney(turtle)
        elif selection == "2":
            draw_house(turtle)
        elif selection == "3":
            draw_roof(turtle)
        elif selection == "4":
            draw_door(turtle)
        elif selection == "5":
            draw_window(turtle)
        elif selection == "6":
            draw_door_knob(turtle)
        elif selection == "r":
            turtle.pen = rg.Pen("red", 3)
        elif selection == "g":
            turtle.pen = rg.Pen("green", 3)
        elif selection == "b":
            turtle.pen = rg.Pen("blue", 3)
        elif selection == "p":
            turtle.pen = rg.pen("purple", 3)
            break
        else:
            print("no such command")


def draw_chimney(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(50, 90))
    turtle.pen_down()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)


def draw_house(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-80, -160))
    turtle.pen_down()
    for k in range(4):
        turtle.forward(160)
        turtle.left(90)


def draw_roof(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-100, 0))
    turtle.pen_down()
    for k in range(3):
        turtle.forward(200)
        turtle.left(120)
def draw_door(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-25, -160))
    turtle.pen_down()
    for k in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

def draw_window(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-20, 30))
    turtle.pen_down()
    for k in range(8):
        turtle.forward(20)
        turtle.left(360 / 8)
def draw_door_knob(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(15, -115))
    turtle.pen_down()
    for k in range(36):
        turtle.forward(1)
        turtle.left(10)



main()