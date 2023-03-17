from global_constants import SKEW_LIST, BADGE_ASSETS_DIRECTORY
import os

import display

# ------------------------------
#      Badge settings
# ------------------------------

WIDTH, HEIGHT = display.WIDTH, display.HEIGHT
IMAGE_WIDTH = 120

# Layout settings
BORDER_SIZE = 3
COMPANY_HEIGHT = 40
    

# ------------------------------
#      Badge functions
# ------------------------------


def draw_badge_text(skew: str = "normal"):
    # Clear the Display
    display.clear(display.BLACK)

    badge_file = [
            f
            for f in os.listdir(f"/{BADGE_ASSETS_DIRECTORY}/{skew}")
            if f.endswith(".txt")
        ][0]
        
    with open(f"/{BADGE_ASSETS_DIRECTORY}/{skew}/{badge_file}", "r") as f:
        company = f.readline()
        name = f.readline()
        detail1 = f.readline()
        detail2 = f.readline()
        detail3 = f.readline()
        detail4 = f.readline()
    
    PADDING = 10
    LEFT_PADDING = 27
    
    REMAINING = (HEIGHT - 120)//4

    # draw background
    display.draw_rectangle(
        display.BACKGROUND,
        BORDER_SIZE,
        BORDER_SIZE,
        WIDTH - (BORDER_SIZE * 2),
        HEIGHT - (BORDER_SIZE * 2)
    )

    display.nb_flag(BORDER_SIZE, 120, 120, WIDTH - 120)

    # draw header box
    display.draw_rectangle(
        display.TITLEBAR,
        BORDER_SIZE,
        BORDER_SIZE,
        WIDTH - (BORDER_SIZE * 2),
        COMPANY_HEIGHT
    )

    # draw names below header
    display.draw_rectangle(
        display.BLACK,
        0,
        COMPANY_HEIGHT + BORDER_SIZE,
        WIDTH,
        BORDER_SIZE
    )

    # draw header text
    display.draw_text(company, "bitmap6", display.BLACK, 17, BORDER_SIZE + 2, WIDTH, 5)

    # Draw name background
    display.trans_flag(
        BORDER_SIZE,
        COMPANY_HEIGHT + BORDER_SIZE * 2,
        76,
        WIDTH - IMAGE_WIDTH - 3 * BORDER_SIZE,
    )

    # draw name text
    display.draw_text(name, "bitmap14_outline", display.BLACK, 12, COMPANY_HEIGHT + 2, WIDTH, 6)
    
    # draw line below name
    display.draw_rectangle(display.BLACK, 0, 120, WIDTH - IMAGE_WIDTH, BORDER_SIZE)    

    # draws the blurb text
    display.draw_text(detail1, "bitmap6", display.BLACK, PADDING, 119 + PADDING, WIDTH, 2)
    display.draw_text(detail2, "bitmap6", display.BLACK, PADDING, 119 + REMAINING + PADDING, WIDTH, 2)
    display.draw_text(detail3, "bitmap6", display.BLACK, PADDING, 119 + 2 * REMAINING + PADDING, WIDTH, 2)
    display.draw_text(detail4, "bitmap6", display.BACKGROUND, PADDING, 119 + 3 * REMAINING + PADDING, WIDTH, 2)
    
    # Draws a line separating the image
    display.draw_rectangle(
        display.BLACK,
        WIDTH - (2 * BORDER_SIZE + IMAGE_WIDTH),
        COMPANY_HEIGHT + BORDER_SIZE,
        BORDER_SIZE,
        HEIGHT
    )
            

def draw_badge_image(index: int = 0, skew: str = "normal"):

    try:
        badge_images = [
            f
            for f in os.listdir(f"/{BADGE_ASSETS_DIRECTORY}/{skew}")
            if f.endswith(".jpg")
        ]
    except OSError:
        print(f"No badge images found for skew {skew}.")
        return
    
    if len(badge_images) == 0:
        print(f"No badge images found for skew {skew}.")
        return
    
    image_path = f"/{BADGE_ASSETS_DIRECTORY}/{skew}/{badge_images[index % len(badge_images)]}"

    display.draw_image(
        image_path,
        WIDTH - IMAGE_WIDTH - BORDER_SIZE,
        COMPANY_HEIGHT + 2 * BORDER_SIZE
    )
    
    display.update()

if __name__ == "__main__":
    draw_badge_text()
    draw_badge_image()