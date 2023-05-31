import rosegraphics as rg


def main():
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("blue", 3)
    turtle.speed = 20  # Optional - Faster!

    while True:
        selection = input("Select an option: ")
        if selection == "1":
            draw_house(turtle)  # box (2nd)
        elif selection == "2":
            draw_roof(turtle)  # triangle (3rd)
        elif selection == "3":
            draw_door(turtle)  # rectangle (4th)
        elif selection == "4":
            draw_window(turtle)  # octagon (5th)
        elif selection == "5":
            draw_doorknob(turtle)  # 'circle' (6th)
        elif selection == "6":
            draw_chimney(turtle)  # 2 lines (1st)
        elif selection == "r":
            turtle.pen = rg.Pen("red", 3)
        elif selection == "g":
            turtle.pen = rg.Pen("green", 3)
        elif selection == "b":
            turtle.pen = rg.Pen("blue", 3)
        elif selection == "":
            break
        else:
            print("Not a valid option")

    print("Goodbye!")


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


def draw_doorknob(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(12, -115))
    turtle.pen_down()
    for k in range(36):
        turtle.forward(1)
        turtle.left(360 / 36)


main()
