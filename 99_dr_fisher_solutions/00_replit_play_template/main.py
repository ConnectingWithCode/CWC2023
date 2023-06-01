# From:
# https://github.com/replit/play


import play

cat = play.new_text('=^.^=', font_size=70)


@play.repeat_forever
async def move_cat():
    cat.x = play.random_number(-200, 200)
    cat.y = play.random_number(-200, 200)
    cat.color = play.random_color()

    cat.show()

    await play.timer(seconds=0.8)

    cat.hide()

    await play.timer(seconds=0.4)


@cat.when_clicked
def win_function():
    cat.show()
    cat.words = 'You won!'


play.start_program()
