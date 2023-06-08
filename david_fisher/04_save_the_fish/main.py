import play
import random

background = play.new_image("underwater.png")
message = play.new_text("Hello World", y=250, color="cyan")
diver = play.new_image("diver.png", size=33, x=-250)

fish_list = []
for k in range(10):
    fish = play.new_image("fish.png", size=33, x=-300, y=random.randint(-250, 250))
    fish.speed_y = random.randint(2, 5)
    fish.speed_x = random.randint(2, 5)
    fish_list.append(fish)

trash = play.new_image("trash.png", size=25)

@play.repeat_forever
def main_loop():
    diver.point_towards(play.mouse)
    diver.move(5)
    for fish in fish_list:
        fish.x += fish.speed_x
        fish.y += fish.speed_y
        if abs(fish.y) > 290:
            fish.speed_y *= -1
        if abs(fish.x) > 390:
            fish.speed_x *= -1














play.start_program()
