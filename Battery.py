import psutil
import time
from BrokenLeaf_TTS import speak
import threading
from Alert import Alert

battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        time.sleep(10)
        percentage = int(battery.percent)
        plugged_in = battery.power_plugged
        if percentage == 100 and plugged_in:
            t1 = threading.Thread(target=Alert, args=("Battery Fully Charged🔋🔋",))
            t2 = threading.Thread(target=speak, args=("Sir, Battery is charged, please unplug the charger!!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 60 and not plugged_in:
            t1 = threading.Thread(target=Alert, args=("60% Battery remaining",))
            t2 = threading.Thread(target=speak, args=("Sir, 60% Battery is remaining, please plug the charger!!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 40 and not plugged_in:
            t1 = threading.Thread(target=Alert, args=("Low Battery⚠️⚠️",))
            t2 = threading.Thread(target=speak, args=("Sir, Battery is Low, please plug the charger!!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 20 and not plugged_in:
            t1 = threading.Thread(target=Alert, args=("Sir Battery is almost dead🪫🪫",))
            t2 = threading.Thread(target=speak, args=("Sir, Battery is very low, please plug the charger!!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            pass

def percentage_checker():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    t1 = threading.Thread(target=Alert, args=(f"The device is running at {percent}% power...",))
    t2 = threading.Thread(target=speak, args=(f"Supreme, the device is running at {percent}% power",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def check_plug():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                t1 = threading.Thread(target=Alert, args=(f"Charging Started...🟢",))
                t2 = threading.Thread(target=speak, args=(f"Charging started",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
            else:
                t1 = threading.Thread(target=Alert, args=(f"Charging Stopped...🔴",))
                t2 = threading.Thread(target=speak, args=(f"Charging stopped",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()

        previous_state = battery.power_plugged