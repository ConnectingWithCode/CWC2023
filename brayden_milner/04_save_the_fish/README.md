If you need any links for this project we'll put them below:

---
**Replit Play library**

https://github.com/replit/play

---

    import play

    cat = play.new_text('=^.^=', font_size=70)

    @play.repeat_forever
    def main_loop():
        cat.color = play.random_color()
    
    @play.repeat_forever
    async def move_cat():
        cat.show()
        await play.timer(seconds=0.5)

        cat.hide()
        await play.timer(seconds=0.4)


    play.start_program()


---
**Slides**

[Save the Fish](https://docs.google.com/presentation/d/16NNG0fWXGmKSYs48OTEPZ4MalQVeZWuDhJWps-FRn1Q/edit?usp=share_link)

---