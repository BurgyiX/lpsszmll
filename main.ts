input.onButtonPressed(Button.A, function () {
    lépés = 0
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.ThreeG, function () {
    lépés += 1
})
let lépés = 0
lépés = 0
basic.forever(function () {
    basic.showNumber(lépés)
    led.stopAnimation()
})
