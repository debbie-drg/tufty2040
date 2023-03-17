import display

options = [
    "a. Badge",
    "b. QR",
    "c. Gallery",
    "a. & c. Stickers",
]


def draw_menu_image():
    try:
        display.draw_image("menu.jpg", 0, 0)
    except OSError:
        print("Menu image not found")


def show_options():
    for line, option in enumerate(options):
        display.draw_rounded_rectangle(
            display.BACKGROUND, 10, 10 + 38 * line, 230, 28, 3
        )
        display.draw_text(option, "bitmap6", display.PURPLE, 15, 13 + 38 * line, 240, 3)


def draw_menu():
    display.clear(display.BACKGROUND)
    draw_menu_image()
    show_options()
    display.update()


if __name__ == "__main__":
    draw_menu()
