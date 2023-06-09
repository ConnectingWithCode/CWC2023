import play
import random

background = play.new_image("background.png")
message = play.new_text("Please Recycle: Save the City!", y=280, color="darkgreen")
bin = play.new_image("recycle.png", size=75, y=-250)
bin.is_trash_bin = False
bin.ground = 0
bin.correct = 0
bin.incorrect = 0
bin.is_game_over = False


# trash_list = []
#
# @play.repeat_forever
# async def loop_with_a_timer():
#     if diver.is_game_over:
#         return
#     trash = play.new_image("trash.png", size=25, x=450, y=random.randint(-250, 250))
#     trash_list.append(trash)
#     await play.timer(seconds=0.5)
#
#
#

@play.repeat_forever
def main_loop():
    if bin.is_game_over:
        return
    if play.key_is_pressed("right", "d"):
        bin.x += 15
    if play.key_is_pressed("left", "a"):
        bin.x -= 15
    if play.key_is_pressed("r"):
        bin.image = "recycle.png"
        bin.is_trash_bin = False
    if play.key_is_pressed("t"):
        bin.image = "trash.png"
        bin.is_trash_bin = True


#     for fish in fish_list:
#         fish.x += fish.speed_x
#         fish.y += fish.speed_y
#         if abs(fish.y) > 290:
#             fish.speed_y *= -1
#         if abs(fish.x) > 390:
#             fish.speed_x *= -1
#
#     for trash in trash_list:
#         trash.x -= 3
#         if diver.is_touching(trash):
#             trash_list.remove(trash)
#             trash.remove()
#             diver.score += 1
#             message.words = f"Score = {diver.score}"
#         if trash.x < -450:
#             trash_list.remove(trash)
#             trash.remove()
#
#     for fish in fish_list:
#         for trash in trash_list:
#             if fish.is_touching(trash):
#                 trash_list.remove(trash)
#                 fish_list.remove(fish)
#                 trash.remove()
#                 fish.remove()
#                 if len(fish_list) == 0:
#                     diver.is_game_over = True


play.start_program()
