import play
import random

print("Save the Fish")

play.new_image("underwater.png")

diver = play.new_image("diver.png", x=-350, y=-250, size=33)
diver.game_over = False

message = play.new_text("3", x=-300, y=275, color='yellow')

jars = []

@play.repeat_forever
async def create_jars():
    jar = play.new_image("jar.png", x=400, y=random.randint(-275, 275))
    jars.append(jar)
    await play.timer(seconds=0.8)

fishies = []
for k in range(3):
    fish = play.new_image("fish.png", x=-350, y=-275 + k * 275, size=33)
    fish.speed_x = 1
    fish.speed_y = 2
    fishies.append(fish)

@play.repeat_forever
def forever_loop():
    if diver.game_over:
        message.words = "Game over"
        return
    diver.point_towards(play.mouse)
    diver.move(5)

    for jar in jars:
        jar.x = jar.x - 3
        if jar.is_touching(diver):
            jars.remove(jar)
            jar.remove()

    for fish in fishies:
        fish.x = fish.x + fish.speed_x
        fish.y = fish.y + fish.speed_y
        if abs(fish.y) > 280:
            fish.speed_y *= -1
        if abs(fish.x) > 380:
            fish.speed_x *= -1

        for jar in jars:
            if fish.is_touching(jar):
                fishies.remove(fish)
                fish.remove()
                message.words = len(fishies)

        if len(fishies) == 0:
            diver.game_over = True


play.start_program()