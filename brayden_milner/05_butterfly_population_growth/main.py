import random
import play
import time

play.new_image("background.png")

score_text = play.new_text("Butterflies = 10", x=0, y=250, font_size=40, color='purple')
time_text = play.new_text("Timer = 0", x=0, y=280, font_size=40, color='purple')

butterfly = play.new_image("butterfly.png", x=-200, y=-200, size=60)

butterfly.game_over = False
butterfly.counter = 10

start_time = time.time()
MAX_TIME = 30

bubble_list = []
bubble_images = [
    "bubble_div2.png",
    "bubble_minus4.png",
    "bubble_minus8.png",
    "bubble_mult2.png",
    "bubble_plus4.png"]

@play.repeat_forever
async def create_bubbles():
    if butterfly.game_over:
        return
    costume_number = random.randint(0, 4)
    bubble_left = play.new_image(bubble_images[costume_number],
                                 x=-200,
                                 y=300,
                                 size=35)
    bubble_left.costume_number = costume_number

    costume_number = random.randint(0, 4)
    bubble_right = play.new_image(bubble_images[costume_number],
                                 x=200,
                                 y=300,
                                 size=35)
    bubble_right.costume_number = costume_number

    bubble_list.append(bubble_left)
    bubble_list.append(bubble_right)
    await play.timer(seconds=8)

@play.repeat_forever
def control_motion():
    if butterfly.game_over:
        score_text.words = f"Final Butterflies = {butterfly.counter}"
        if butterfly.counter <= 0:
            score_text.words = f"Butterflies = {butterfly.counter}. You lose!"
        return
    time_text.words = f"Timer = {(time.time() - start_time):.2f}"
    if time.time() - start_time > MAX_TIME:
        butterfly.game_over = True
    if play.key_is_pressed("left", "a"):
        butterfly.x = -200
    elif play.key_is_pressed("right", "d"):
        butterfly.x = 200
    for bubble in bubble_list:
        bubble.y -= 4
        if bubble.is_touching(butterfly):
            if bubble.costume_number == 0:
                butterfly.counter /= 2
            elif bubble.costume_number == 1:
                butterfly.counter -= 4
            elif bubble.costume_number == 2:
                butterfly.counter -= 8
            elif bubble.costume_number == 3:
                butterfly.counter *= 2
            elif bubble.costume_number == 4:
                butterfly.counter += 4
            score_text.words = f"Butterflies = {butterfly.counter}"
            bubble_list.remove(bubble)
            bubble.remove()
        elif bubble.y < -76:
            bubble_list.remove(bubble)
            bubble.remove()

play.start_program()