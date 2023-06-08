import play
import random

play.new_image("background.png")

# Testing images before we start:
# recyclable = play.new_image("milk.png", x=-200, y=-200, size=60)
# recyclable = play.new_image("waterglass.png", x=-200, y=-200, size=60)
# trash = play.new_image("tennisball.png", x=200, y=-200, size=60)
# trash = play.new_image("shoes.png", x=200, y=-200, size=80)

bin = play.new_image("recycle.png", x=0, y=-200, size=80)
bin.isTrash = False  # because we start with recycling
bin.caughtCorrectly = 0
bin.caughtIncorrectly = 0
bin.hitGround = 0
bin.game_over = False

scoreboard = play.new_text(
  "CaughtCorrectly = 0   CaughtIncorrectly = 0   HitGround = 0",
  x=-60,
  y=280,
  font_size=25,
  color='purple')


you_win_message = play.new_text(
  "You Win!",
  x=0,
  y=180,
  font_size=250,
  color='yellow')
you_win_message.hide()


@play.repeat_forever
def control_bin():
  if bin.game_over:
    return
  if play.key_is_pressed("left", "a"):
    bin.x = bin.x - 15
  elif play.key_is_pressed("right", "d"):
    bin.x = bin.x + 15
  if play.key_is_pressed("t"):
    bin.isTrash = True
    bin.image = "chromebook.png"
  elif play.key_is_pressed("r"):
    bin.isTrash = False
    bin.image = "recycle.png"


falling_items = []


def generate_trash():
  trash_images = ["tennisball.png", "shoes.png"]
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
  recyclable_images = ["milk.png", "waterglass.png"]
  if random.random() < 0.5:
    image_filename = recyclable_images[0]
  else:
    image_filename = recyclable_images[1]

  item = play.new_image(image_filename,
                        x=random.randint(-300, 300),
                        y=600,
                        size=35)
  item.isTrash = False
  falling_items.append(item)


@play.repeat_forever
async def create_objects():
  if bin.game_over:
    return
  if random.random() < 0.5:
    generate_trash()
  else:
    generate_recycling()
  await play.timer(seconds=2)


@play.repeat_forever
def control_motion():
  if bin.game_over:
    return
  for item in falling_items:
    item.y = item.y - 4
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
  scoreboard.words = f"CaughtCorrectly = {bin.caughtCorrectly}   CaughtIncorrectly = {bin.caughtIncorrectly}   HitGround = {bin.hitGround}"

play.start_program()
