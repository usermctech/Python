import pyautogui
import time
time.sleep(3)
distance = 0
while distance > 200:
    pyautogui.drag(distance, 0, duration=0.1)   # move right
    distance -= 2
    pyautogui.drag(0, distance, duration=0.1)   # move down
    pyautogui.drag(-distance, 0, duration=0.1)  # move left
    distance -= 2
    pyautogui.drag(0, -distance, duration=0.1)  # move up