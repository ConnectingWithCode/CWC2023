import play

cwc_text = play.new_text("William Cracraft", y=-200, color=(0,255,0), font_size=100)

my_message = play.new_text("is cool", y=-250, color="green")



kit_cat = play.new_image("my_image.png", x=50, y=150, size=50)
glitch_cat = play.new_image("kitten.webp", x=0, y=0, size=20)
glitch_2 = play.new_image("kitten.webp", x=100, y=100, size=20)
catty = play.new_image("catty.png", x=-80, y=210, size=15)
catty_2 = play.new_image("catty.png", x=100, y=-210, size=15)
kit_cat_2 = play.new_image("kit_cat.png", x=-100, y=-50, size=50)
grey = play.new_image("grey.webp", x=-200, y=-70, size=100)
grey_2 = play.new_image("grey.webp", x=-400, y=260, size=100)

@play.repeat_forever
def main_loop():
    glitch_cat.angle += 5
    grey.angle += 100
    grey_2.angle += 100
    glitch_2.angle += 5
    kit_cat_2.angle += 10
    kit_cat.angle += 10
    catty.angle += 25
    catty_2.angle += 25
    cwc_text.size -= 0.2
    if cwc_text.size < 0:
        cwc_text.size = 100


@play.repeat_forever
async def loop_with_a_timer():
    cwc_text.color = play.random_color()
    my_message.color = play.random_color()
    grey.color = play.random_color()
    await play.timer(seconds=0.5)
    

play.start_program()
