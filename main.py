import time

from global_constants import (
    SKEW_LIST,
    ALTERNATE_GALLERY_SKEWS,
    BRIGHTNESS_UPDATE_INTERVAL_MS,
)

from autobrightness import auto_brightness

NUMBER_SKEWS = len(SKEW_LIST)
NUMBER_ALTERNATE_GALLERIES = len(ALTERNATE_GALLERY_SKEWS)

import buttons, menu, badge, qr, gallery


def update_content(state: dict) -> None:
    mode = state["mode"]
    current_index = state["index"]
    skew = state["skew"]

    if mode == "badge":
        if state["mode_change"]:
            badge.draw_badge_text(skew)
        badge.draw_badge_image(current_index, skew)

    if mode == "qr":
        qr.draw_qr_file(current_index, skew)

    if mode == "gallery":
        gallery.show_image(current_index, skew)
        
    if state["mode_change"]:
        state["mode_change"] = False
        time.sleep(0.3)


def buttons_abc(state: dict) -> bool:
    a_pressed = buttons.is_pressed("a")
    b_pressed = buttons.is_pressed("b")
    c_pressed = buttons.is_pressed("c")


    if any([a_pressed, b_pressed, c_pressed]):
        state["mode_change"] = True

        if a_pressed and not c_pressed:
            state["mode"] = "badge"

        if c_pressed and not a_pressed:
            state["mode"] = "gallery"

        if b_pressed:
            state["mode"] = "qr"

        if a_pressed and c_pressed:
            state["mode"] = "gallery"
            state["gallery_index"] += 1
            if NUMBER_ALTERNATE_GALLERIES > 0:
                state["gallery_index"] = (
                    state["gallery_index"] % NUMBER_ALTERNATE_GALLERIES
                )
                state["skew"] = ALTERNATE_GALLERY_SKEWS[state["gallery_index"]]
            else:
                print("Tried to access alternate galleries but none has been defined.")
                pass
        else:
            if state["skew"] in ALTERNATE_GALLERY_SKEWS:
                state["skew"] = SKEW_LIST[0]

        state["index"] = 0

        return True

    return False


def buttons_updown(state: dict) -> bool:

    up_pressed = buttons.is_pressed("up")
    down_pressed = buttons.is_pressed("down")

    if up_pressed:
        state["index"] += 1
        state["mode_change"] = False

    if down_pressed:
        state["index"] -= 1
        state["mode_change"] = False

    if up_pressed and down_pressed:
        state["mode_change"] = True

        if state["skew"] in ALTERNATE_GALLERY_SKEWS:
            state["skew"] = SKEW_LIST[0]
        else:
            state["skew_index"] += 1
            state["skew_index"] = state["skew_index"] % NUMBER_SKEWS
            state["skew"] = SKEW_LIST[state["skew_index"]]

        state["index"] = 0

    if up_pressed or down_pressed:
        return True

    return False


def main_loop():
    
    last_brightness_update = -1
    
    state = {
        "mode": "menu",
        "skew": "normal",
        "index": 0,
        "skew_index": 0,
        "gallery_index": 0,
        "mode_change": False,
    }

    menu.draw_menu()

    while True:
        
        time_ms = time.ticks_ms()
        if time_ms - last_brightness_update > BRIGHTNESS_UPDATE_INTERVAL_MS:
            auto_brightness()
            last_brightness_update = time_ms
               
        if buttons_abc(state) or buttons_updown(state):
            update_content(state)
            time.sleep(0.2)


# ------------------------------
#       Main program
# ------------------------------

if __name__ == "__main__":
    main_loop()
