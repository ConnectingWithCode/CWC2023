import play
import random

backround = play.new_image("background.png")
message = play.new_text("cats", y=250, color="orange")
bin = play.new_image("trash.png", size=75, y=-250)
bin.is_trash_bin = True
bin.ground = 0
bin.correct = 0
bin.incorrect = 0
bin.is_game_over = False


falling_items_list = []

@play.repeat_forever
async def loop_with_a_timer():
    if bin.is_game_over:
        return

    item_number = random.randint(1,2)
    print(item_number)

    if item_number == 1:
        falling_item = play.new_image("bannana.png", size=50)
        falling_item.is_trash = True

    if item_number == 2:
        falling_item = play.new_image("cat.png", size=50)
        falling_item.is_trash = False

    falling_item.y = 280
    falling_item.x = random.randint(-350, 350)
    falling_items_list.append(falling_item)
    await play.timer(seconds=2)





@play.repeat_forever
def main_loop():
    if bin.is_game_over:
        return
    if play.key_is_pressed("right"):
        bin.x += 25
    if bin.x > 350:
        bin.x = 350
    if play.key_is_pressed("left"):
        bin.x -= 25
    if bin.x < -350:
        bin.x = -350



    if play.key_is_pressed("r"):
        bin.image = "recycle.png"
        bin.is_trash_bin = False
    if play.key_is_pressed("t"):
        bin.image = "trash.png"
        bin.is_trash_bin = True


    for falling_item in falling_items_list:
        falling_item.y -=2
        if falling_item.y < -250:
            bin.ground += 1
            falling_items_list.remove(falling_item)
            falling_item.remove()
        if bin.is_touching(falling_item):
            if bin.is_trash_bin == falling_item.is_trash:
                bin.correct += 1
            else:
                bin.incorrect += 1
            falling_items_list.remove(falling_item)
            falling_item.remove()



    if bin.incorrect + bin.ground > 9:
        bin.is_game_over = True

    message.words = f"good: {bin.correct} bad: {bin.incorrect} on the ground: {bin.ground}"







play.start_program()
