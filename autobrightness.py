from machine import ADC
from display import set_brightness

lux = ADC(26)
last_brightness = 1


def light_level():
    return lux.read_u16()


def auto_brightness():
    lux_level = light_level()
    brightness = ((lux_level / 5000) ** 0.4) * 0.63 + 0.32
    set_brightness(brightness)
