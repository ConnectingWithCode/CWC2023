import play
import random

background = play.new_image("underwater.png")
message = play.new_text("Save the Fish!", y=280, color="cyan")
diver = play.new_image("diver.png", size=33, x=-250)
diver.score = 0
diver.is_game_over = False

fish_list = []
for k in range(10):
    fish = play.new_image("fish.png", size=33, x=-300, y=random.randint(-250, 250))
    fish.speed_y = random.randint(2, 5)
    fish.speed_x = random.randint(2, 5)
    fish_list.append(fish)

# trash = play.new_image("trash.png", size=25)
trash_list = []

@play.repeat_forever
async def loop_with_a_timer():
    if diver.is_game_over:
        return
    trash = play.new_image("trash.png", size=25, x=450, y=random.randint(-250, 250))
    trash_list.append(trash)
    await play.timer(seconds=0.5)



@play.repeat_forever
def main_loop():
    if diver.is_game_over:
        return
    diver.point_towards(play.mouse)
    diver.move(5)

    for fish in fish_list:
        fish.x += fish.speed_x
        fish.y += fish.speed_y
        if abs(fish.y) > 290:
            fish.speed_y *= -1
        if abs(fish.x) > 390:
            fish.speed_x *= -1

    for trash in trash_list:
        trash.x -= 3
        if diver.is_touching(trash):
            trash_list.remove(trash)
            trash.remove()
            diver.score += 1
            message.words = f"Score = {diver.score}"
        if trash.x < -450:
            trash_list.remove(trash)
            trash.remove()

    for fish in fish_list:
        for trash in trash_list:
            if fish.is_touching(trash):
                trash_list.remove(trash)
                fish_list.remove(fish)
                trash.remove()
                fish.remove()
                if len(fish_list) == 0:
                    diver.is_game_over = True












play.start_program()
