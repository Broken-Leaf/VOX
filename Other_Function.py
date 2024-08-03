import pyautogui as gui
import time
import pywhatkit


def search_on_youtube(text):
    gui.press("/")
    time.sleep(0.9)
    gui.write(text)
    time.sleep(0.5)
    gui.press("enter")

def search_on_google(text):
    pywhatkit.search(text)


