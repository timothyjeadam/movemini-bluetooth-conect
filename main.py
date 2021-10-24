def on_bluetooth_connected():
    basic.show_leds("""
        # # . # #
                # # . # #
                . . # . .
                # . . . #
                . # # # .
    """)
    basic.show_string("MY NAME IS ZEZOT")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
    ServoLite.stop()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_mes_dpad_controller_id_microbit_evt():
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        ServoLite.forward()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_UP:
        ServoLite.stop()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        ServoLite.backward()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_UP:
        ServoLite.stop()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        ServoLite.left()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_UP:
        ServoLite.stop()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        ServoLite.right()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_UP:
        ServoLite.stop()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        pins.set_audio_pin(AnalogPin.P3)
        music.play_melody("A B A B A B A B ", 120)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        ServoLite.set_distance_per_second(100)
        ServoLite.drive_forwards(100)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . # # #
                        # # # # #
                        # . # # #
        """)
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        for index in range(2):
            basic.show_string("90=50+40")
            basic.show_string("10+10=20")
            break
            continue
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)
