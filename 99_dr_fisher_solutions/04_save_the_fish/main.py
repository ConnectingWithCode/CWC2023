import play
import random
import time

play.new_image("underwater.png")
message = play.new_text("Fish remaining = 3",
                        color="yellow",
                        font_size=30,
                        y = 280)

diver = play.new_image("diver.png",
                      x=-350,
                      size=33)

diver.is_game_over = False
diver.start_time = time.time()
diver.end_time = 0

fish_list = []
for k in range(3):
  fish = play.new_image("fish.png",
                       x=-350,
                       y=random.randint(-275, 275),
                       size=33)
  fish.speed_x = random.randint(1, 4)
  fish.speed_y = random.randint(3, 6)
  fish_list.append(fish)

jar_list = []

@play.repeat_forever
async def create_jar():
  if diver.is_game_over:
    return
  jar = play.new_image("jar.png",
                      x=400,
                      y=random.randint(-280, 280),
                      size=50)
  jar_list.append(jar)
  await play.timer(seconds=1.0)


@play.repeat_forever
def forever_loop():
  if diver.is_game_over:
    message.words = f"Game over! Time = {diver.end_time - diver.start_time:.1f} seconds."
    return

  diver.point_towards(play.mouse)
  diver.move(5)

  for fish in fish_list:
    fish.x += fish.speed_x
    fish.y += fish.speed_y
    if abs(fish.x) > 380:
      fish.speed_x *= -1
    if abs(fish.y) > 280:
      fish.speed_y *= -1

  for jar in jar_list:
    jar.x -= 3
    if jar.is_touching(diver):
      jar_list.remove(jar)
      jar.remove()
    if jar.x < -400:
      jar_list.remove(jar)
      jar.remove()

  for fish in fish_list:
    for jar in jar_list:
      if fish.is_touching(jar):
        jar_list.remove(jar)
        jar.remove()
        fish_list.remove(fish)
        fish.remove()
        message.words = f"Fish remaining = {len(fish_list)}"

  if len(fish_list) == 0:
    diver.is_game_over = True
    diver.end_time = time.time()

play.start_program()