let moisture = 0
OLED.init(128, 64)
basic.forever(function () {
    moisture = smarthome.ReadSoilHumidity(AnalogPin.P1)
    OLED.clear()
    OLED.writeStringNewLine("Moisture:")
    OLED.writeNumNewLine(moisture)
    basic.pause(500)
})
