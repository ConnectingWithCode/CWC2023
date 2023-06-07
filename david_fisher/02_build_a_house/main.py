import rosegraphics as rg


def jump_to(turtle, x, y):
    turtle.pen_up()
    turtle.go_to(rg.Point(x, y))
    turtle.set_heading(0)
    turtle.pen_down()


def draw_chimney(turtle):
    jump_to(turtle, 50, 90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)


def draw_box(turtle):
    jump_to(turtle, -80, -160)
    for k in range(4):
        turtle.forward(160)
        turtle.left(90)


def main():
    print("Build a House")
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("orange", 5)

    while True:
        selection = input("Selection: ")
        if selection == "1":
            draw_chimney(turtle)
        if selection == "2":
            draw_box(turtle)
        if selection == "r":
            turtle.pen = rg.Pen("red", 5)
        if selection == "g":
            turtle.pen = rg.Pen("green", 5)
        if selection == "o":
            turtle.pen = rg.Pen("orange", 5)
        if selection == "p":
            turtle.pen = rg.Pen("purple", 5)
        if selection == "y":
            turtle.pen = rg.Pen("yellow", 5)
        if selection == "":
            break


main()
