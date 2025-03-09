from gpiozero import Button
from gpiozero import LED
import threading
import time
import logging

class Gpio:
    POWER_BUTTON_PIN = 12  # StandBy-On
    MENU_BUTTON_PIN = 13   # Open/Close
    LEFT_BUTTON_PIN = 5    # Play/Pause
    RIGHT_BUTTON_PIN = 6   # Stop
    RELAY_PIN = 4

    def __init__(self, buttons_enabled, on_power, on_menu, on_left, on_right, relay_enabled):
        self._lock = threading.Lock()

        if (buttons_enabled):
            b1 = Button(self.POWER_BUTTON_PIN)
            b2 = Button(self.MENU_BUTTON_PIN)
            b3 = Button(self.LEFT_BUTTON_PIN)
            b4 = Button(self.RIGHT_BUTTON_PIN)

            b1.when_pressed = lambda gpio: on_power() if not self._lock.locked() else None
            b2.when_pressed = lambda gpio: on_menu() if not self._lock.locked() else None
            b3.when_pressed = lambda gpio: on_left() if not self._lock.locked() else None
            b4.when_pressed = lambda gpio: on_right() if not self._lock.locked() else None

        if (relay_enabled):
            self._is_relay_on = False
            self.relay = LED(self.RELAY_PIN)

        self._relay_enabled = relay_enabled

    def switch_relay(self, value):
        if (self._relay_enabled and self._lock.acquire()):
            try:
                if (value != self._is_relay_on):
                    if (value):
                        self.relay.on()
                    else:
                        self.relay.off()
                    self._is_relay_on = value
                    time.sleep(1)
                    return True
            except Exception as inst:
                logging.error(inst)
            finally:
                threading.Timer(1, self._lock.release).start()
        return False
