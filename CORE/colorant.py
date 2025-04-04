import os
from typing import Literal
import cv2
import numpy as np
import threading
import time
import win32api

from .screen_cap import ScreenCapture
from .mouse import ArduinoMouse


class Colorant:
    PURPLE_LOWER_COLOR = np.array([140, 110, 150])
    PURPLE_UPPER_COLOR = np.array([150, 195, 255])

    RED_LOWER_COLOR = np.array([165, 100, 100])
    RED_UPPER_COLOR = np.array([180, 255, 255])

    YELLOW_LOWER_COLOR = np.array([20, 150, 100])
    YELLOW_UPPER_COLOR = np.array([40, 255, 255])

    def __init__(self, x, y, grabzone, mouse_sensitivity, border_color: Literal["purple", "red", "yellow"], hold_key):
        self.arduinomouse = ArduinoMouse()
        self.grabber = ScreenCapture(x, y, grabzone)
        self.mouse_sensitivity = mouse_sensitivity
        self.hold_key = hold_key
        if border_color == "purple":
            self.LOWER_COLOR = self.PURPLE_LOWER_COLOR
            self.UPPER_COLOR = self.PURPLE_UPPER_COLOR
        elif border_color == "red":
            self.LOWER_COLOR = self.RED_LOWER_COLOR
            self.UPPER_COLOR = self.RED_UPPER_COLOR
        elif border_color == "yellow":
            self.LOWER_COLOR = self.YELLOW_LOWER_COLOR
            self.UPPER_COLOR = self.YELLOW_UPPER_COLOR
        threading.Thread(target=self.run, daemon=True).start()
        self.toggled = False

<<<<<<< HEAD

=======
>>>>>>> 2bf25f9bbc42197e92023d77541f89c3d81d34b5
    def toggle(self):
        self.toggled = not self.toggled
        time.sleep(0.2)

    def run(self):
        while True:
            if win32api.GetAsyncKeyState(self.hold_key) < 0 and self.toggled:
                self.process("move")

    def process(self, action):
        screen = self.grabber.get_screen()
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.LOWER_COLOR, self.UPPER_COLOR)
        dilated = cv2.dilate(mask, None, iterations=6)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if not contours:
            return

        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        center = (x + w // 2, y + h // 2)

        if action == "move":
            cX = x + w // 2
            cY = y + 9
            x_diff = cX - self.grabber.grabzone // 2
            y_diff = cY - self.grabber.grabzone // 2
<<<<<<< HEAD
            self.arduinomouse.move(x_diff * self.mouse_sensitivity, y_diff * self.mouse_sensitivity)
=======
            self.arduinomouse.move(x_diff * 0.2, y_diff * 0.2)
>>>>>>> 2bf25f9bbc42197e92023d77541f89c3d81d34b5

    def close(self):
        if hasattr(self, 'arduinomouse'):
            self.arduinomouse.close()
        self.toggled = False

    def __del__(self):
        self.close()
