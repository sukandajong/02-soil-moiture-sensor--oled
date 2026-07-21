moisture = 0
OLED.init(128, 64)

def on_forever():
    global moisture
    moisture = smarthome.read_soil_humidity(AnalogPin.P1)
    OLED.clear()
    OLED.write_string_new_line("Moisture:")
    OLED.write_num_new_line(smarthome.read_soil_humidity(AnalogPin.P1))
    basic.pause(500)
basic.forever(on_forever)
