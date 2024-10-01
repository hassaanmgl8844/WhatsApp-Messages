import time
import pyautogui as auto

print("Initiating...")

time.sleep(5)
print("5 seconds passed")
a = 0
while a < 1515:
    auto.write("Write Your Message")
    auto.press("enter")
    print(a)
    a = a + 1