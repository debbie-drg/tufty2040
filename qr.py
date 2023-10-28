import display, qrcode
import os

WIDTH, HEIGHT = display.WIDTH, display.HEIGHT
HEADER_HEIGHT = 40
BORDER = 3
PADDING = 4

from global_constants import QR_CODE_DIRECTORY

code = qrcode.QRCode()

# ------------------------------
#        QR Code Functions
# ------------------------------


def measure_qr_code(size: int, code: qrcode.QRCode) -> tuple(int, int):
    w, h = code.get_size()
    module_size = int(size / w)
    return module_size * w, module_size


def draw_qr_code(ox: int, oy: int, size: int, code: qrcode.QRCode) -> None:
    size, module_size = measure_qr_code(size, code)
    display.draw_rectangle(display.BACKGROUND, ox, oy, size, size)
    for x in range(size):
        for y in range(size):
            if code.get_module(x, y):
                display.draw_rectangle(
                    display.BLACK,
                    ox + x * module_size,
                    oy + y * module_size,
                    module_size,
                    module_size,
                )


def draw_qr_file(index: int = 0, skew: str = "normal") -> None:
    try:
        CODES = [
            f for f in os.listdir(f"/{QR_CODE_DIRECTORY}/{skew}") if f.endswith(".txt")
        ]
    except OSError:
        print(f"No QR codes found for skew {skew}")
        return

    if len(CODES) == 0:
        print(f"No QR codes in skew {skew}. Code will not be printed.")
        return

    index = index % len(CODES)
    file = CODES[index]

    codetext = open(f"{QR_CODE_DIRECTORY}/{skew}/{file}", "r")
    lines = codetext.read().strip().split("\n")
    codetext.close()

    code_text = lines.pop(0)
    title_text = lines.pop(0)
    detail_text = lines

    # Clear the Display
    display.clear(display.BACKGROUND)

    code.set_text(code_text)
    size, _ = measure_qr_code(HEIGHT - 2 * HEADER_HEIGHT, code)
    left = PADDING + BORDER
    top = int((HEIGHT // 2) - (size // 2))
    draw_qr_code(left, top, HEIGHT - 2 * HEADER_HEIGHT, code)

    display.trans_flag(
        size + 2 * PADDING + BORDER,
        HEADER_HEIGHT + BORDER,
        HEIGHT - 2 * HEADER_HEIGHT - BORDER + 4,
        WIDTH - size - 2 * BORDER - 2 * PADDING,
    )

    # Draw a border around the screen and code
    display.draw_border(display.BLACK, BORDER)
    display.draw_rectangle(
        display.BLACK,
        size + BORDER + 2 * PADDING,
        HEADER_HEIGHT,
        BORDER,
        HEIGHT - HEADER_HEIGHT,
    )

    # Draw headers
    display.draw_rectangle(
        display.TITLEBAR, BORDER, BORDER, WIDTH - (BORDER * 2), HEADER_HEIGHT - BORDER
    )

    # Line below header
    display.draw_rectangle(display.BLACK, 0, HEADER_HEIGHT, WIDTH, BORDER)

    # Draw botton bar
    display.draw_rectangle(
        display.TITLEBAR,
        BORDER,
        HEIGHT - HEADER_HEIGHT,
        WIDTH - (BORDER * 2),
        HEADER_HEIGHT - BORDER,
    )

    # Line above bottom
    display.draw_rectangle(display.BLACK, 0, HEIGHT - HEADER_HEIGHT, WIDTH, BORDER)

    # Header text
    display.draw_centered_text(title_text, "bitmap6", display.BLACK, 0, 8, WIDTH, 5)

    # Bottom text
    display.draw_text(
        "Scan the QR!!",
        "bitmap6",
        display.BLACK,
        PADDING + BORDER,
        HEIGHT - HEADER_HEIGHT + 2,
        WIDTH,
        5,
    )

    number_details = len(detail_text)
    remaining_height = HEIGHT - 2 * HEADER_HEIGHT
    space_per_detail = remaining_height // number_details

    for detail_index, detail in enumerate(detail_text):
        display.draw_text(
            detail,
            "bitmap6",
            display.BLACK,
            5 * PADDING + BORDER + size,
            HEADER_HEIGHT + 12 + detail_index * space_per_detail,
            WIDTH - PADDING - BORDER - size,
            2,
        )

    # This would draw squares hinting to the number of QR codes and to
    # which one is active
    if len(CODES) > 1:
        for i in range(len(CODES)):
            x = WIDTH - 20
            y = int((HEIGHT / 2) - (len(CODES) * 10 / 2) + (i * 14))
            display.draw_rectangle(display.BLACK, x, y, 12, 12)
            if index != i:
                display.draw_rectangle(display.BACKGROUND, x + 2, y + 2, 8, 8)

    display.update()


# Main programme for testing purposes
if __name__ == "__main__":
    draw_qr_file()
