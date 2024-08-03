import webbrowser
import pyautogui as ui
import time
from Automation.App_opener import open_App

def play_music_on_spotify(song_name):
    open_App("spotify")
    time.sleep(3.5)
    ui.hotkey("ctrl", "l")
    time.sleep(1)
    ui.write(song_name)
    time.sleep(2)
    ui.leftClick(953, 490)
    time.sleep(1.3)
    ui.press("enter")

def play_my_playlist(text):
    if "play my playlist" in text or "play playlist" in text or "play my favorite playlist" in text or "play my favorite songs" in text or "playlist" in text or "my playlist" in text or "I want to listen to my playlist" in text or "i want to listen to my playlist" in text or "I want to listen to my favourite songs" in text or "I want to listen to my favourite playlist" in text or "meri playlist chalao" in text or "mere songs chalao" in text or "meri favorite playlist chalao" in text or "playlist chalao" in text or "favorite songs chalao" in text or "mere gaane sunao" in text or "mera favourite playlist lagao" in text or "mera playlist lagao" in text or "mera playlist bajao" in text or "mera favourite playlist bajao" in text or "mere favourite gaane bajao" in text or "mera playlist bajao" in text:
        webbrowser.open("https://open.spotify.com/playlist/3a52uyYW3swiJ6AQVdjDBw")
        time.sleep(3.5)
        ui.leftClick(560, 642)
    else:
        pass

def multiple_functions(text):
    if "next" in text or "skip" in text or "play next" in text or "next song" in text or "play next song" in text or "skip to next song" in text or "skip to next" in text or "skip this one" in text or "next gaana" in text or "next song chalao" in text or "next gaana bajao" in text or "next gaana sunao" in text or "next" in text or "next song" in text or "skip gaana" in text or "skip song" in text or "dusra gaana lagao" in text or "dusra gaana bajao" in text or "ye gaana skip karo" in text or "gaana skip karo" in text:
        ui.hotkey("ctrl", "right arrow")
    elif "last" in text or "back" in text or "previous" in text or "previous song" in text or "play previous song again" in text or "skip to previous song" in text or "skip to previous" in text or "skip to previous one" in text or "play again" in text or "play last song" in text or "last song" in text or "play this one again" in text or "play previous song" in text or "pichla gaana" in text or "pichla gaana chalao" in text or "pichla gaana bajao" in text or "pichla gaana sunao" in text or "last gaana" in text:
        ui.hotkey("ctrl", "left arrow")
    elif "play" in text or "pause" in text or "stop" in text or "stop this song" in text or "stop this one" in text or "resume" in text or "play again" in text or "resume again" in text or "play" in text or "pause" in text or "stop" in text or "stop gaana" in text or "stop this gaana" in text or "phir se play karo" in text or "phir se chalu karo" in text or "bajao" or "roko" in text or "play karo" in text:
        ui.hotkey("space")
    elif "repeat" in text or "repeat this song" in text or "repeat this one" in text or "repeat this" in text or "repeat" in text or "repeat gaana" in text or "ye gaana repeat karo" in text or "is gaane ko dohrao" in text or "gaana dohrao" in text or "ye gaana repeat karo" in text or "is gaana ko repeat karo" in text or "ye gaana repeat karo" in text or "repeat karo isko":
        ui.hotkey("ctrl", "r")
    else:
        pass
