import play
import random

play.new_image("background.png", size=150)

play.new_text(f"Linear Lights Out",
              y=200,
              font_size=100,
              color='yellow')

score_text = play.new_text(f"You won in _ moves!",
                           y=100,
                           font_size=50,
                           color='yellow')
score_text.hide()

light_list = []
light_images = ["light_on.png", "light_off.png"]

you_win_light = play.new_image(light_images[0],
                               x=0,
                               y=-150,
                               size=75)
you_win_light.game_over = False
you_win_light.isOn = True
you_win_light.counter = 0
you_win_light.hide()

for k in range(7):
    if random.random() < 0.5:
        image_filename = light_images[0]
        image_number = 0
    else:
        image_filename = light_images[1]
        image_number = 1

    light = play.new_image(image_filename,
                           x=-300 + k * 100,
                           y=0,
                           size=50)
    if image_number == 0:
        light.isOn = True
    else:
        light.isOn = False
    light.num = k
    light_list.append(light)


@play.repeat_forever
async def control_lights():
    if you_win_light.game_over:
        if not you_win_light.isOn:
            you_win_light.image = light_images[1]
        score_text.words = f"You won in {you_win_light.counter} moves!"
        if you_win_light.counter == 1:
            score_text.words = f"You won in {you_win_light.counter} move!"
        score_text.show()
        you_win_light.show()
        return
    for light in light_list:
        if play.mouse.is_clicked:
            if play.mouse.is_touching(light):
                if light.num == 0:
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num + 1])
                    you_win_light.counter += 1
                elif light.num == 6:
                    toggle_light(light_list[light.num - 1])
                    toggle_light(light_list[light.num])
                    you_win_light.counter += 1
                else:
                    toggle_light(light_list[light.num - 1])
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num + 1])
                    you_win_light.counter += 1
                await play.timer(seconds=0.1)

    on_counter = 0
    off_counter = 0
    for light in light_list:
        if light.isOn:
            on_counter += 1
        else:
            off_counter += 1

    if on_counter == len(light_list):
        you_win_light.game_over = True
        you_win_light.isOn = True
    elif off_counter == len(light_list):
        you_win_light.game_over = True
        you_win_light.isOn = False


def toggle_light(light):
    if light.isOn:
        light.image = light_images[1]
        light.isOn = False
    else:
        light.image = light_images[0]
        light.isOn = True


play.start_program()
