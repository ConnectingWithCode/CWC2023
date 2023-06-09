import play

cwc_text = play.new_text("Parker Auman", y=-200, color=(250,250,250), font_size=100)

my_message = play.new_text("are cool", y=-260)

#cwc_logo = play.new_image("cwc_logo.png", x=0, y=100, size=50)
cat = play.new_image("cat.png", size=100, y= 50)

100@play.repeat_forever
def main_loop():
    cat.angle -= 1
    #cwc_text.size -= .2
    if cwc_text.size < 0:
        cwc_text.size =


@play.repeat_forever
async def loop_with_a_timer():
   # cwc_text.color = play.random_color()
    await play.timer(seconds=0.5)


play.start_program()