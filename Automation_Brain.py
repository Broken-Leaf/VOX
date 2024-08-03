from Automation.App_opener import open_App
from Automation.Web_Opener import open_Web
import pyautogui as gui
from Automation.Play_Music_YT import play_music_on_youtube
from Automation.Play_Music_SFY import play_music_on_spotify
from Automation.Play_Music_SFY import play_my_playlist
from Automation.Play_Music_SFY import multiple_functions
from BrokenLeaf_TTS import speak
from Automation.Battery import percentage_checker
from os import getcwd
from Automation.Other_Function import search_on_youtube, search_on_google
from Automation.Tab_Automation import execute_command
from Automation.Youtube_Playback import execute_media_command
from Automation.Scroll_integration import execute_scroll_command
import time
    
def close(text):
    if "close tab" in text or "close this tab" in text or "just close this tab" in text or "ye tab band karo" in text or "tab band karo" in text or "tab close karo" in text or "tab ko band karo" in text or "ye tab close karo" in text:
        gui.hotkey("ctrl", "w")
    elif "close window" in text or "close this window" in text or "close" in text or "just close this window" in text or "close" in text or "close window" in text or "ye window band karo" in text or "window band karo" in text or "window close karo" in text or "window ko band karo" in text or "ye window close karo" in text:
        gui.hotkey("alt", "f4")
    else:
        pass

def Open_Brain(text):
    if "website" in text or "open website" in text or "open web" in text or "just open website" in text:
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website", "").strip()
        text = text.replace("open web", "").strip()
        text = text.replace("just open website", "").strip()
        open_Web(text)
    else:
        text = text.replace("open", "").strip()
        text = text.replace("app", "").strip()
        text = text.replace("just open", "").strip()
        text = text.replace("open app", "").strip()
        text = text.replace("open", "").strip()
        open_App(text)

def clear_file():
    with open(f"{getcwd()}\\input.txt", "w") as file:
        file.truncate(0)

def Auto_main_brain(text):
    try:
        if text.startswith("open"):
            Open_Brain(text)
        elif "close" in text:
            close(text)
        elif "play one music on youtube" in text or "play music on youtube" in text or "play some music on youtube" in text or "youtube pe gaana chalao" in text or "youtube pe gaana" in text or "youtube pe gaana sunao" in text or "youtube pe gaana bajao" in text or "youtube pe gaana" in text or "gaana bajao youtube pe" in text or "gaana chalao youtube pe" in text or "gaana sunao youtube pe" in text:
            speak("which song do you want to play?")
            time.sleep(2)
            clear_file()
            output_text = ""
            while True:
                with open("input.txt", "r") as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text:
                        play_music_on_youtube(output_text)
                        break
        elif "play music" in text or "play music on spotify" in text or "play some music" in text or "i want to listen some music" in text or "i want to listen music" in text or "spotify pe gaana bajao" in text or "gaana bajao" in text or "spotify pe gaana chalao" in text or "gaana chalao" in text or "spotify pe gaana sunao" in text or "gaana sunao" in text or "gaana bajao spotify pe" in text:
            speak("which song do you want to play?")
            time.sleep(2)
            clear_file()
            output_text = ""
            while True:
                with open("input.txt", "r") as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text:
                        play_music_on_spotify(output_text)
                        break
        elif "play my playlist" in text or "play playlist" in text or "play my favorite playlist" in text or "play my favorite songs" in text or "playlist" in text or "my playlist" in text or "I want to listen to my playlist" in text or "i want to listen to my playlist" in text or "I want to listen to my favourite songs" in text or "I want to listen to my favourite playlist" in text or "meri playlist chalao" in text or "mere songs chalao" in text or "meri favorite playlist chalao" in text or "playlist chalao" in text or "favorite songs chalao" in text or "mere gaane sunao" in text or "mera favourite playlist lagao" in text or "mera playlist lagao" in text or "mera playlist bajao" in text or "mera favourite playlist bajao" in text or "mere favourite gaane bajao" in text or "mera playlist bajao" in text:
            speak("Playing, Supreme.")
            play_my_playlist(text)
        elif "next" in text or "skip" in text or "play next" in text or "next song" in text or "play next song" in text or "skip to next song" in text or "skip to next" in text or "skip this one" in text or "next gaana" in text or "next song chalao" in text or "next gaana bajao" in text or "next gaana sunao" in text or "next" in text or "next song" in text or "skip gaana" in text or "skip song" in text or "dusra gaana lagao" in text or "dusra gaana bajao" in text or "ye gaana skip karo" in text or "gaana skip karo" in text:
            multiple_functions(text)
        elif "last" in text or "back" in text or "previous" in text or "previous song" in text or "play previous song again" in text or "skip to previous song" in text or "skip to previous" in text or "skip to previous one" in text or "play again" in text or "play last song" in text or "last song" in text or "play this one again" in text or "play previous song" in text or "pichla gaana" in text or "pichla gaana chalao" in text or "pichla gaana bajao" in text or "pichla gaana sunao" in text or "last gaana" in text:
            multiple_functions(text)
        elif "play" in text or "pause" in text or "stop" in text or "stop this song" in text or "stop this one" in text or "resume" in text or "play again" in text or "resume again" in text or "play" in text or "pause" in text or "stop" in text or "stop gaana" in text or "stop this gaana" in text or "phir se play karo" in text or "phir se chalu karo" in text or "bajao" or "roko" in text or "play karo" in text:
            multiple_functions(text)
        elif "repeat" in text or "repeat this song" in text or "repeat this one" in text or "repeat this" in text or "repeat" in text or "repeat this gaana" in text or "ye gaana repeat karo" in text or "is gaane ko dohrao" in text or "gaana dohrao" in text or "ye gaana repeat karo" in text or "is gaana ko repeat karo" in text or "ye gaana repeat karo" in text or "repeat karo isko":
            multiple_functions(text)  
        elif "battery" in text or "check battery percentage" in text or "what's the battery percentage" in text or "check battery level" in text or "battery level" in text or "check battery" in text:
            percentage_checker(text)
        elif text.startswith("search"):
            text = text.replace("search", "")
            text = text.replace("for", "")
            search_on_youtube(text)
        elif "search on Google" in text or "search on Google that" in text or "search on Google about" in text or "search on Google for" in text or "search on google" in text or "search on google that" in text or "search on google about" in text or "search on google for" in text or "search karo" in text or "search karo ki":
            text = text.replace("search on google", "")
            text = text.replace("search on google that", "")
            text = text.replace("search on google about", "")
            text = text.replace("search on google for", "")
            text = text.replace("search on Google", "")
            text = text.replace("search on Google that", "")
            text = text.replace("search on Google about", "")
            text = text.replace("search on Google for", "")
            text = text.replace("search karo", "")
            text = text.replace("search karo ki", "")
            search_on_google(text)
        else:
            execute_command(text)
            execute_media_command(text)
            execute_scroll_command(text)

    except Exception as e:
        print(e)
