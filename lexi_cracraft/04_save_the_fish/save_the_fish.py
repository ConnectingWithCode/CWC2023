import play
import random

print("Save the Fish")
play.new_image("underwater.png")

diver = play.new_image("diver.png", x=350, y=250, size=33,)
diver.game_over = False

message = play.new_text("3", x=300, y=275, color='white',)
jar_list = []

@play.repeat_forever
async def create_jars():
    jar = play.new_image("jar.png", x=400, y=random.randint(-275, 275))
    jar_list.append(jar)
    await play.timer(seconds=0.8)

fish_list = []
for k in range(3):
    fish = play.new_image("fish.png", x=-350, y=-275 + k * 275, size=33)
    fish.speed_x = 1
    fish.speed_y = 2
    fish_list.append(fish)

@play.repeat_forever
def forever_loop():
    if diver.game_over:
        message.words = "Game over"
        return
    diver.point_towards(play.mouse)
    diver.move(5)

    for jar in jar_list:
        jar.x -= 3
        if jar.is_touching(diver):
            jar_list.remove(jar)
            jar.remove()

    for fish in fish_list:
        fish.x += fish.speed_x
        fish.y += fish.speed_y
        if abs(fish.x) > 380:
            fish.speed_x *= -1
        if abs(fish.y) > 280:
            fish.speed_y *= -1

        for jar in jar_list:
            if fish.is_touching(jar):
                fish_list.remove(fish)
                fish.remove()
                message.words = len(fish_list)

            if len(fish_list) == 0:
                diver.game_over = True

play.start_program()
