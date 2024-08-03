import pyautogui

def scroll_up():
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')

def scroll_down():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

def scroll_to_top():
    pyautogui.hotkey('home')

def scroll_to_bottom():
    pyautogui.hotkey('end')

def execute_scroll_command(text):
    if text in [
        "scroll up", "move up", "scroll upwards", "go up", "move upwards", "up scroll", "scroll higher", "scroll up page", 
        "page up", "scroll up by five", "scroll up multiple times", "scrolling up", "scroll up more", "scroll up now", "scroll upwards page", 
        "upar scroll karo", "upar move karo", "upar scroll", "page ko upar scroll karo", "scroll upar", "upar jaye", "upar scroll", 
        "scroll ko upar karo", "scroll ko upar move karo", "scroll ko upar badhao", "upar badhao", "upar scroll karo", "scroll upar karo", 
        "upar move karo", "scroll ko upar jao"
    ]:
        scroll_up()
    elif text in [
        "scroll down", "move down", "scroll downwards", "go down", "move downwards", "down scroll", "scroll lower", "scroll down page", 
        "page down", "scroll down by five", "scroll down multiple times", "scrolling down", "scroll down more", "scroll down now", "scroll down page", 
        "neeche scroll karo", "neeche move karo", "neeche scroll", "page ko neeche scroll karo", "scroll neeche", "neeche jaye", "neeche scroll", 
        "scroll ko neeche karo", "scroll ko neeche move karo", "scroll ko neeche badhao", "neeche badhao", "neeche scroll karo", "scroll neeche karo", 
        "neeche move karo", "scroll ko neeche jao"
    ]:
        scroll_down()
    elif text in [
        "scroll to top", "move to top", "go to top", "scroll up to top", "move up to top", "top of the page", "scroll to beginning", 
        "scroll to start", "top scroll", "jump to top", "scroll beginning", "scroll home", "scroll to home", "top of page", "scroll home now", 
        "upar ke top par jaye", "shuru par jaye", "shuru me jaye", "scroll ko upar le jao", "scroll ko shuru karo", "top par scroll karo", 
        "scroll ko shuru me le jao", "scroll home par jaye", "scroll ko top le jao", "top par move karo", "scroll ko top par le jao", 
        "scroll ko top me le jao", "shuru par le jao", "scroll home par le jao"
    ]:
        scroll_to_top()
    elif text in [
        "scroll to bottom", "move to bottom", "go to bottom", "scroll down to bottom", "move down to bottom", "bottom of the page", 
        "scroll to end", "scroll to finish", "bottom scroll", "jump to bottom", "scroll end", "scroll finish", "bottom of page", 
        "scroll to end now", "neeche ke bottom par jaye", "ant par jaye", "ant me jaye", "scroll ko neeche le jao", "scroll ko end karo", 
        "bottom par scroll karo", "scroll ko ant me le jao", "scroll bottom par jaye", "scroll ko bottom par le jao", "scroll ko end me le jao", 
        "neeche ke end par le jao", "scroll end par le jao", "scroll ko bottom me le jao"
    ]:
        scroll_to_bottom()
    else:
        pass
