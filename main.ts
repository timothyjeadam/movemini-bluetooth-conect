bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        # # . # #
        # # . # #
        . . # . .
        # . . . #
        . # # # .
        `)
    basic.showString("MY NAME IS ZEZOT")
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
    ServoLite.stop()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        ServoLite.forward()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_UP) {
        ServoLite.stop()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        ServoLite.backward()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_UP) {
        ServoLite.stop()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        ServoLite.left()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_UP) {
        ServoLite.stop()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        ServoLite.right()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_UP) {
        ServoLite.stop()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN) {
        pins.setAudioPin(AnalogPin.P3)
        music.playMelody("A B A B A B A B ", 120)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_UP) {
        ServoLite.stop()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . # # #
            # # # # #
            # . # # #
            `)
        basic.showArrow(ArrowNames.West)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN) {
        for (let index = 0; index < 2; index++) {
            basic.showString("90=50+40")
            basic.showString("10+10=20")
            break;
continue;
        }
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_UP) {
        ServoLite.stop()
    }
})
