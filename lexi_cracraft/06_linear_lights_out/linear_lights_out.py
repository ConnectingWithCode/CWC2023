import play
import random

play.new_image("background.png", size=150)

final_timer = 0

title_text = play.new_text(f"Linear Lights Out",
              y=200,
              font_size=100,
              color='yellow')

score_text = play.new_text(f"You won in _ moves!",
                           y=100,
                           font_size=50,
                           color='yellow')

score_text.hide()

win_light = play.new_image("light_on.png",
                           y=-150,
                           size=75)
win_light.game_over = False
win_light.isOn = True
win_light.counter = 0
win_light.hide()

win_light.time = 0
timer = True

time_text = play.new_text(f"{win_light.time}",
                          y=70,
                          font_size=40,
                          color='yellow')
time_text.hide()

@play.repeat_forever
async def timer():
    while timer:
        win_light.time += 1
        time_text.words = f"{win_light.time}"
        await play.timer(seconds=1)

light_list = []
light_images = ["light_on.png", "light_off.png"]

for k in range(7):
    if random.random() < 0.5:
        image_filename = light_images[0]
        image_number = 0
    else:
        image_filename = light_images[1]
        image_number = 1
    light = play.new_image(image_filename,
                           x=-300 + k * 100,
                           size=50)
    light.num = k
    if image_number == 0:
        light.isOn = True
    else:
        light.isOn = False
    light_list.append(light)

@play.repeat_forever
async def control_lights():
    if win_light.game_over:
        timer = False
        time_text.show()
        if not win_light.isOn:
            win_light.image = light_images[1]
        score_text.words = f"You won in {win_light.counter} moves!"
        score_text.show()
        if not win_light.isOn:
            score_text.color = 'black'
            title_text.color = 'black'
            time_text.color = 'black'
        if win_light.counter == 1:
            score_text.words = f"You won in 1 move!"
        win_light.show()
        return
    for light in light_list:
        if play.mouse.is_clicked:
            if play.mouse.is_touching(light):
                win_light.counter += 1
                if light.num == 0:
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num + 1])
                elif light.num == 6:
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num - 1])
                else:
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num - 1])
                    toggle_light(light_list[light.num + 1])
                await play.timer(seconds=0.25)
    on_counter = 0
    off_counter = 0
    for light in light_list:
        if light.isOn:
            on_counter += 1
        else:
            off_counter += 1

    if on_counter == len(light_list):
        win_light.game_over = True
        win_light.isOn = True
    elif off_counter == len(light_list):
        win_light.game_over = True
        win_light.isOn = False

def toggle_light(light):
    if light.isOn:
        light.image = light_images[1]
        light.isOn = False
    else:
        light.image = light_images[0]
        light.isOn = True

play.start_program()