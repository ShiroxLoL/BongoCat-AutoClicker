import pydirectinput
import time
import keyboard
import random

pydirectinput.PAUSE = 0  # Keine extra Pausen

print("Press 'p' to start/stop - made by ShiroxLoL")
time.sleep(5)

min_interval = 0.01  # min. Intervall (Seconds)
max_interval = 0.02  # max. Intervall (Seconds)
hold_time = 0.02     # Hold Time (0.02s for Bypass)
running = False

def toggle_running():
    global running
    running = not running
    if running:
        print("Auto-Clicker started.")
    else:
        print("Auto-Clicker stopped.")

keyboard.add_hotkey('p', toggle_running)  # 'p' = Start/Stop

while not keyboard.is_pressed('q'):
    if running:
        # Simuliere einen vollständigen Klick mit Hold
        pydirectinput.mouseDown()  # button='left' default
        # Falls Koordinaten: pydirectinput.mouseDown(x=x, y=y)
        time.sleep(hold_time)
        pydirectinput.mouseUp()
        
        # Zufälliges Intervall für nächsten Klick
        time.sleep(random.uniform(min_interval, max_interval))
    
    time.sleep(0.01)  # Schleifen um CPU zu schonen

print("Script stopped.")