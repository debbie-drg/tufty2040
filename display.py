from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from jpegdec import JPEG

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
j = JPEG(display)

WIDTH, HEIGHT = display.get_bounds()

last_brightness = -1


def set_brightness(brightness):
    global last_brightness
    if brightness >= 1:
        brightness = 0.99
    elif brightness <= 0.35:
        brightness = 0.37
    if abs(brightness - last_brightness) >= 0.05:
        last_brigthness = brightness
        display.set_backlight(brightness)  # has to be between .3 and .99


# Colours
BACKGROUND = display.create_pen(255, 255, 255)
TITLEBAR = display.create_pen(200, 0, 0)
BLACK = display.create_pen(0, 0, 0)
YELLOW = display.create_pen(252, 244, 52)
PURPLE = display.create_pen(156, 89, 209)
BLUE = display.create_pen(91, 206, 250)
PINK = display.create_pen(245, 169, 184)


def clear(color):
    display.set_pen(color)
    display.clear()


def trans_flag(x_coord, y_coord, height, width):
    per_bar, remainder = divmod(height, 5)
    display.set_pen(BLUE)
    display.rectangle(x_coord, y_coord, width, per_bar)
    display.rectangle(x_coord, y_coord + 4 * per_bar, width, per_bar)
    display.set_pen(PINK)
    display.rectangle(x_coord, y_coord + per_bar, width, per_bar)
    display.rectangle(x_coord, y_coord + 3 * per_bar, width, per_bar)
    display.set_pen(BACKGROUND)
    display.rectangle(x_coord, y_coord + 2 * per_bar, width, per_bar + remainder)


def nb_flag(x_coord, y_coord, height, width):
    per_bar = height // 4
    display.set_pen(YELLOW)
    display.rectangle(x_coord, y_coord, width, per_bar)
    display.set_pen(BACKGROUND)
    display.rectangle(x_coord, y_coord + per_bar, width, per_bar)
    display.set_pen(PURPLE)
    display.rectangle(x_coord, y_coord + 2 * per_bar, width, per_bar)
    display.set_pen(BLACK)
    display.rectangle(x_coord, y_coord + 3 * per_bar, width, per_bar)


def draw_rectangle(color, x_coord, y_coord, width, height):
    display.set_pen(color)
    display.rectangle(x_coord, y_coord, width, height)


def draw_background(color):
    display.set_pen(color)
    display.rectangle(0, 0, WIDTH, HEIGHT)


def draw_rounded_rectangle(color, x_coord, y_coord, width, height, radius):
    display.set_pen(color)

    display.rectangle(x_coord + radius, y_coord, width - radius * 2, height)
    display.rectangle(x_coord, y_coord + radius, width, height - radius * 2)

    display.circle(x_coord + radius, y_coord + radius, radius)
    display.circle(x_coord + width - radius - 1, y_coord + radius, radius)
    display.circle(x_coord + radius, y_coord + height - radius - 1, radius)
    display.circle(x_coord + width - radius - 1, y_coord + height - radius - 1, radius)


def draw_border(color, width):
    display.set_pen(color)
    display.rectangle(0, 0, width, HEIGHT)
    display.rectangle(0, 0, WIDTH, width)
    display.rectangle(WIDTH - width, 0, width, HEIGHT)
    display.rectangle(0, HEIGHT - width, WIDTH, width)


def draw_text(text: str, font: str, color, x_coord, y_coord, width, size):
    display.set_pen(color)
    display.set_font(font)
    display.text(text, x_coord, y_coord, width, size)


def draw_image(image_path, x_coord, y_coord):
    j.open_file(image_path)
    j.decode(x_coord, y_coord)


def update():
    display.update()


if __name__ == "__main__":
    nb_flag(0, 0, HEIGHT, WIDTH)
    display.update()
