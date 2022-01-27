import pyautogui
import time
a = 1000
b = 1

time.sleep(1)
time.sleep(0.5)
#było while
while a < b:
    pyautogui.write(("Pętla for="+str(i)))
    pyautogui.press('enter')
    b = b+1


