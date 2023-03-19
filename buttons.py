from pimoroni import Button

buttons = {
    "a": 7,
    "b": 8,
    "c": 9,
    "up": 22,
    "down": 6,
}

def is_pressed(button: str) -> bool:
    try:
        return Button(buttons[button], invert=False).is_pressed
    except KeyError:
        print("Invalid button.")
        
