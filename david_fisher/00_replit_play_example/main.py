import play

cwc_text = play.new_text("Dave Fisher", y=-200, color=(128,0,0), font_size=100)
my_message = play.new_text("is cool", y=-260, color=(227, 66, 52), font_size=60)

cwc_logo = play.new_image("cwc_logo.png", y=100, size=50)
my_image = play.new_image("my_image.png", size=30)

@play.repeat_forever
def main_loop():
    # cwc_logo.angle += 0.5
    # cwc_text.size -= 0.2
    if cwc_text.size < 0:
        cwc_text.size = 100


@play.repeat_forever
async def loop_with_a_timer():
    # cwc_text.color = play.random_color()
    await play.timer(seconds=0.5)


play.start_program()
