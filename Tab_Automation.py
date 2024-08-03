import pyautogui

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('fn', 'f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')

def execute_command(text):
    if text in [
        "open new tab", "new tab", "create tab", "add tab", "open tab", "launch new tab", "new browser tab",
        "start new tab", "make new tab", "initiate new tab", "generate new tab", "new browsing tab", "spawn new tab",
        "activate new tab", "bring up new tab", "tab new", "naya tab kholo", "tab kholo", "tab naya kholo", 
        "tab shuru karo", "tab bana lo", "tab add karo", "tab open karo", "naya tab", "browser tab naya kholo", 
        "tab ko shuru karo", "tab ko bana lo", "tab ko add karo", "tab ko kholo", "tab shuru karna", "tab banaye", 
        "tab naya shuru karo","naya page kholo", "page kholo", "page naya kholo", "page shuru karo", "page bana lo",
    ]:
        open_new_tab()
    elif text in [
        "close this tab", "shut tab", "terminate tab", "exit tab", "kill tab", "delete tab", "end tab", "discard tab", 
        "remove tab", "close current tab", "shut current tab", "terminate current tab", "exit current tab", 
        "kill current tab", "delete current tab", "tab band karo", "band tab", "tab bandh karo", "bandh tab", 
        "terminate tab karo", "tab ko bandh karo", "tab ko band", "tab ko exit karo", "exit tab karo", 
        "delete tab karo", "tab ko delete karo", "tab ko terminate karo", "tab ko end karo", "end tab karo", 
        "tab ko discard karo", "close current tab", "close tab karo", "tab ko close karo", "tab ko remove karo",
    ]:
        close_tab()
    elif text in [
        "open browser menu", "open menu", "browser menu", "launch menu", "show menu", "access menu", "display menu", 
        "menu options", "open settings menu", "browser settings", "browser options", "browser settings menu", 
        "launch browser menu", "access browser menu", "display browser menu", "menu kholo", "browser menu kholo", 
        "menu open karo", "menu launch karo", "menu dikhaye", "menu access karo", "menu display karo", 
        "menu ke options", "settings menu kholo", "browser settings kholo", "browser options kholo", 
        "browser settings menu kholo", "browser menu access karo", "browser menu display karo"
    ]:
        open_browser_menu()
    elif text in [
        "zoom in", "increase zoom", "enlarge", "magnify", "make bigger", "make larger", "increase size", 
        "zoom closer", "zoom larger", "zoom more", "zoom to in", "make zoom in", "zoom in more", "zoom bigger", 
        "zoom bigger in", "zoom", "zoomin", "magnify screen", "screen bada karo", "screen zoom karo", 
        "zoom bada karo", "zoom screen", "zoom screen in", "screen ko bada karo", "screen ko magnify karo", 
        "zoom in screen", "screen ko zoom karo", "zoom in karna", "zoom karna", "zoom ko in karo"
    ]:
        zoom_in()
    elif text in [
        "zoom out", "decrease zoom", "shrink", "reduce", "make smaller", "make tinier", "decrease size", 
        "zoom away", "zoom smaller", "zoom less", "zoom to out", "make zoom out", "zoom out more", "zoom tiny", 
        "zoom smaller out", "zoomout", "zoom out screen", "screen chhota karo", "screen ko zoom out karo", 
        "screen chhoti karo", "screen kam karo", "zoom chhota karo", "zoom kam karo", "zoom ko kam karo", 
        "zoom ko out karo", "screen kam zoom karo", "screen ko kam zoom karo", "zoom out karna", "zoom out screen karo", 
        "screen zoom out karo"
    ]:
        zoom_out()
    elif text in [
        "refresh page", "reload page", "refresh", "reload", "refresh current page", "reload current page", "update page", 
        "update current page", "renew page", "renew current page", "refresh site", "reload site", "update site", 
        "renew site", "refresh this page", "page refresh karo", "refresh page karo", "reload page karo", "page ko reload karo", 
        "refresh karo", "page ko refresh karo", "current page refresh karo", "current page reload karo", "page ko update karo", 
        "page ko renew karo", "site ko refresh karo", "site ko reload karo", "site ko update karo", "site ko renew karo", 
        "page ko refresh karna"
    ]:
        refresh_page()
    elif text in [
        "switch to next tab", "next tab", "go to next tab", "move to next tab", "navigate to next tab", "shift to next tab", 
        "change to next tab", "jump to next tab", "switch tab forward", "move tab forward", "navigate tab forward", 
        "shift tab forward", "change tab forward", "jump tab forward", "forward to next tab", "next tab par jaye", 
        "tab agla", "agla tab", "next tab open karo", "next tab switch karo", "next tab chalu karo", "next tab ko kholo", 
        "tab ko agla karo", "tab ko next karo", "tab ko switch karo", "tab ko forward karo", "next tab par jaye", 
        "agla tab open karo", "agla tab switch karo", "next tab chalu karna"
    ]:
        switch_to_next_tab()
    elif text in [
        "switch to previous tab", "previous tab", "go to previous tab", "move to previous tab", "navigate to previous tab", 
        "shift to previous tab", "change to previous tab", "jump to previous tab", "switch tab backward", "move tab backward", 
        "navigate tab backward", "shift tab backward", "change tab backward", "jump tab backward", "backward to previous tab", 
        "pichla tab", "previous tab par jaye", "tab pichla", "pichla tab kholo", "pichla tab switch karo", 
        "pichla tab chalu karo", "pichla tab open karo", "tab ko pichla karo", "tab ko previous karo", "tab ko pichla switch karo", 
        "tab ko back karo", "tab ko backward karo", "previous tab par jaye", "pichla tab ko switch karo", "previous tab open karo"
    ]:
        switch_to_previous_tab()
    elif text in [
        "open history", "view history", "show history", "display history", "history tab", "history page", "browser history", 
        "access history", "check history", "see history", "go to history", "open browsing history", "launch history", 
        "history view", "history display", "history kholo", "browser history kholo", "history dikhaye", "history ko access karo", 
        "history dekho", "history page kholo", "history tab kholo", "history ko display karo", "history ko launch karo", 
        "history ko view karo", "history ko check karo", "history ko dekho", "history ko open karo", "history ko check karna", 
        "history ko access karna"
    ]:
        open_history()
    elif text in [
        "open bookmarks", "view bookmarks", "show bookmarks", "display bookmarks", "bookmarks tab", "bookmarks page", 
        "browser bookmarks", "access bookmarks", "check bookmarks", "see bookmarks", "go to bookmarks", 
        "open browsing bookmarks", "launch bookmarks", "bookmarks view", "bookmarks display", "bookmarks kholo", 
        "browser bookmarks kholo", "bookmarks dikhaye", "bookmarks ko access karo", "bookmarks dekho", "bookmarks page kholo", 
        "bookmarks tab kholo", "bookmarks ko display karo", "bookmarks ko launch karo", "bookmarks ko view karo", 
        "bookmarks ko check karo", "bookmarks ko dekho", "bookmarks ko open karo", "bookmarks ko check karna", 
        "bookmarks ko access karna"
    ]:
        open_bookmarks()
    elif text in [
        "go back", "navigate back", "move back", "return", "backward", "previous page", "last page", "previous", 
        "back a page", "back one page", "go back a page", "navigate back a page", "move back a page", "return to previous", 
        "piche jaye", "peeche", "peeche jao", "pichle page", "pichla page", "page peeche", "page pichla", "previous page par jaye", 
        "page ko peeche karo", "page ko pichla karo", "page ko peeche le jao", "page ko back karo", "page ko back le jao", 
        "back karo", "pichle page par jaye"
    ]:
        go_back()
    elif text in [
        "go forward", "navigate forward", "move forward", "next page", "advance", "proceed", "forward", "forward a page", 
        "forward one page", "go forward a page", "navigate forward a page", "move forward a page", "proceed to next page", 
        "next page par jaye", "aage jaye", "aage jao", "aage badho", "next page kholo", "page aage", "page next", 
        "next page open karo", "page ko next karo", "page ko aage karo", "page ko next le jao", "page ko forward karo", 
        "page ko aage le jao", "next karo", "next le jao", "page ko advance karo"
    ]:
        go_forward()
    elif text in [
        "open dev tools", "developer tools", "dev tools", "open developer tools", "launch dev tools", "launch developer tools", 
        "show dev tools", "show developer tools", "dev tools kholo", "developer tools kholo", "dev tools open karo", 
        "developer tools open karo", "dev tools dikhaye", "developer tools dikhaye", "dev tools ko launch karo", 
        "developer tools ko launch karo", "dev tools ko show karo", "developer tools ko show karo", "dev tools ko access karo", 
        "developer tools ko access karo", "dev tools ko display karo", "developer tools ko display karo", "dev tools ko on karo", 
        "developer tools ko on karo", "dev tools ko shuru karo", "developer tools ko shuru karo", "dev tools ko start karo"
    ]:
        open_dev_tools()
    elif text in [
        "toggle full screen", "full screen", "enter full screen", "exit full screen", "fullscreen mode", "toggle fullscreen mode", 
        "full screen mode", "enter fullscreen mode", "exit fullscreen mode", "launch fullscreen", "fullscreen", "toggle mode", 
        "toggle screen", "screen mode", "fullscreen kholo", "fullscreen band karo", "fullscreen on karo", "fullscreen off karo", 
        "screen full karo", "screen mode full karo", "screen ko full karo", "screen ko band karo", "screen ko on karo", 
        "screen ko off karo", "fullscreen mode chalu karo", "fullscreen mode bandh karo", "fullscreen mode start karo", 
        "fullscreen mode stop karo", "fullscreen mode toggle karo"
    ]:
        toggle_full_screen()
    elif text in [
        "open private window", "new private window", "incognito mode", "open incognito window", "start private window", 
        "launch private window", "open new private window", "launch new private window", "start new private window", 
        "open incognito mode", "start incognito mode", "launch incognito mode", "naya private window kholo", "private window kholo", 
        "private window open karo", "naya incognito mode", "incognito mode kholo", "incognito mode open karo", 
        "incognito window kholo", "naya incognito window", "private window start karo", "naya private window start karo", 
        "private window launch karo", "naya private window launch karo", "naya private window shuru karo", 
        "private window shuru karo", "naya incognito mode start karo", "incognito mode start karo"
    ]:
        open_private_window()
    else:
        pass