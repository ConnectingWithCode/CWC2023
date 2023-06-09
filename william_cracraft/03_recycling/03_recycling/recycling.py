import play
import random

play.new_image("background.png")

bin = play.new_image("recycle.png", x=0, y=-200, size=80)
bin.isTrash = False
bin.game_over = False
bin.caughtCorrectly = 0
bin.caughtIncorrectly = 0
bin.hitGround = 0

scoreboard = play.new_text(
    "CaughtCorrectly = 0     CaughtIncorrectly = 0    HitGround = 0",
    x=-60,
    y=280,
    font_size=25,
    color='green'
)
you_win_message = play.new_text("You Win!", x=0, y=100, font_size = 250, color='yellow')
you_win_message.hide()


@play.repeat_forever
def control_bin():
    if bin.game_over:
        return
    if play.key_is_pressed("left", "a"):
        bin.x -= 15
    elif play.key_is_pressed("right", "d"):
        bin.x +=15
    if play.key_is_pressed("t"):
        bin.isTrash = True
        bin.image = "trash.png"
    elif play.key_is_pressed("r"):
        bin.isTrash = False
        bin.image = "recycle.png"

falling_items = []
def generate_trash():
    trash_images = ["tennisball.png","shoes.png"]
    if random.random() < 0.5:
        image_filename = trash_images[0]
    else:
        image_filename = trash_images[1]

    item = play.new_image(image_filename,
                          x=random.randint(-300, 300),
                          y=600,
                          size=35)
    item.isTrash = True
    falling_items.append(item)



def generate_recycling():
    recyclable_items = ["milk.png", "waterglass.png"]
    if random.random() <0.5:
        image_filename = recyclable_items[0]
    else:
        image_filename = recyclable_items[1]

    item = play.new_(image_filename,
    x=random.randint(-300, 300),
    y=600,
    size = 35)
    item.isTrash = False
    falling_items.append(item)


    @play.repeat_forever
    async def create_objects():
        if bin.game_over:
            return
        else:
            generate_recycling()
            await play.timer(seconds=2)


@play.repeat_forever
  def control_motion():
    if bin.game_over:
      return
    for item in falling_items:
        item.y -= 4
        if item.is_touching(bin):
          if item.isTrash == bin.isTrash:
              bin.caughtCorrectly += 1
          else:
              bin.caughtIncorrectly += 1
          falling_items.remove(item)
          item.remove()
        elif item.y < -225:
            bin.hitGround += 1
            falling_items.remove(item)
            item.remove()

    if bin.caughtCorrectly >= 100:
        you_win_message.show()
        bin.game_over = True
    if bin.caughtIncorrectly + bin.hitGround >= 10:
        bin.game_over = True

    scoreboard.words = f"CaughtCorrectly = {bin.caughtCorrectly}   CaughtIncorrectly = {bin.CaughtIncorrectly} HitGround = {bin.HitGround}"


play.start_program()

