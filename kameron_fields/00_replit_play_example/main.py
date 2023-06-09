import play

cwc_text = play.new_text("Connecting with Code", y=-200, color=(128,0,0), font_size=100)
cwc_logo = play.new_image("cwc_logo.png", x=0, y=100, size=50)


@play.repeat_forever
def main_loop():
    cwc_logo.angle += 0.5
    cwc_text.size -= 0.2
    if cwc_text.size < 0:
        cwc_text.size = 100


@play.repeat_forever
async def loop_with_a_timer():
    cwc_text.color = play.random_color()
    await play.timer(seconds=0.5)


play.start_program()