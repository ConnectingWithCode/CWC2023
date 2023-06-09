import play

cwc_text = play.new_text("Lexi Cracraft", y=-200, color=("orange"), font_size=100)

my_message = play.new_text("is cat", y=-250, color=("teal"), font_size=60)

cwc_logo = play.new_image("my_image.png", x=0, y=100, size=50)
#cwc_logos = play.new_image("cwc_logo.png", x=0, y=-50, size=50)


@play.repeat_forever
def main_loop():
    cwc_logo.angle += 0.5
#    cwc_logos.angle += 0.5
#    cwc_text.size -= 0.2
    if cwc_text.size < 0:
       cwc_text.size = 100


@play.repeat_forever
async def loop_with_a_timer():
    cwc_text.color = play.random_color()
    my_message.color = cwc_text.color
    await play.timer(seconds=0.5)


play.start_program()
