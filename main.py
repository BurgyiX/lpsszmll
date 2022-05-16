def on_button_pressed_a():
    global lépés
    lépés = 0
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_three_g():
    global lépés
    lépés += 1
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

lépés = 0
lépés = 0

def on_forever():
    basic.show_number(lépés)
    led.stop_animation()
basic.forever(on_forever)
