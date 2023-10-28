import display

OPTIONS = [
    "a. Badge",
    "b. QR",
    "c. Gallery",
    "a. & c. Stickers",
]

OPTION_BACKGROUND_COLOURS = [
    display.YELLOW,
    display.BACKGROUND,
    display.PURPLE,
    display.BLACK,
]

OPTION_SPACING = 40
PADDING = 10
TEXT_SPACING = 3
BORDER_SIZE = 4


def draw_menu_image() -> None:
    try:
        display.draw_image("menu.jpg", 0, 0)
    except OSError:
        print("Menu image not found")


def show_options() -> None:
    for line, option in enumerate(OPTIONS):
        display.draw_rounded_rectangle(
            OPTION_BACKGROUND_COLOURS[line],
            PADDING - BORDER_SIZE,
            PADDING + OPTION_SPACING * line - BORDER_SIZE,
            230 + 2 * BORDER_SIZE,
            30 + 2 * BORDER_SIZE - 2,
            3,
        )
        display.draw_rounded_rectangle(
            display.BACKGROUND, PADDING, PADDING + OPTION_SPACING * line, 230, 28, 3
        )
        display.draw_text(
            option,
            "bitmap6",
            display.PURPLE,
            PADDING + TEXT_SPACING,
            13 + OPTION_SPACING * line,
            240,
            3,
        )


def draw_menu() -> None:
    display.clear(display.BACKGROUND)
    draw_menu_image()
    show_options()
    display.update()


if __name__ == "__main__":
    draw_menu()
