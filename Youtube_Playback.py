import pyautogui

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_forward():
    pyautogui.press('right')

def seek_backward():
    pyautogui.press('left')

def seek_forward_10s():
    pyautogui.press('l')

def seek_backward_10s():
    pyautogui.press('j')

def seek_backward_frame():
    pyautogui.press(',')

def seek_forward_frame():
    pyautogui.press('.')

def seek_to_beginning():
    pyautogui.press('home')

def seek_to_end():
    pyautogui.press('end')

def seek_to_previous_chapter():
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    pyautogui.hotkey('shift', 'p')

def execute_media_command(text):
    if text in [
        "volume up", "increase volume", "raise volume", "turn up volume", "make louder", "sound up", "louder", "boost volume", 
        "volume high", "volume raise", "up volume", "more volume", "volume increase", "volume loud", "sound high", 
        "volume badhao", "volume ko badhao", "volume ko increase karo", "volume ko raise karo", "volume ko upar karo", 
        "awaz badhao", "awaz ko badhao", "volume ko high karo", "volume ko loud karo", "volume ko zyada karo", "volume ko boost karo", 
        "sound ko upar karo", "sound badhao", "volume upar karo", "volume ko uncha karo"
    ]:
        volume_up()
    elif text in [
        "volume down", "decrease volume", "lower volume", "turn down volume", "make quieter", "sound down", "quieter", "reduce volume", 
        "volume low", "volume lower", "down volume", "less volume", "volume decrease", "volume quiet", "sound low", 
        "volume kam karo", "volume ko kam karo", "volume ko decrease karo", "volume ko lower karo", "volume ko neeche karo", 
        "awaz kam karo", "awaz ko kam karo", "volume ko low karo", "volume ko quiet karo", "volume ko kam karo", "volume ko reduce karo", 
        "sound ko neeche karo", "sound kam karo", "volume neeche karo", "volume ko neeche le jao"
    ]:
        volume_down()
    elif text in [
        "seek forward", "forward", "move forward", "next", "skip forward", "jump forward", "advance", "move ahead", "proceed forward", 
        "seek ahead", "go forward", "forward seek", "forward move", "seek", "advance forward", 
        "aage badhao", "seek aage", "aage karo", "seek ko aage badhao", "seek ko forward karo", "forward badhao", "forward ko badhao", 
        "forward move karo", "seek ko aage karo", "aage seek karo", "seek ko next karo", "seek ko jump karo", "aage jao", "seek aage karo", 
        "forward seek ko karo"
    ]:
        seek_forward()
    elif text in [
        "seek backward", "backward", "move backward", "previous", "skip backward", "jump backward", "go back", "move back", "retreat", 
        "seek back", "go backward", "backward seek", "backward move", "seek back", "move back", 
        "peeche badhao", "seek peeche", "peeche karo", "seek ko peeche badhao", "seek ko backward karo", "backward badhao", "backward ko badhao", 
        "backward move karo", "seek ko peeche karo", "peeche seek karo", "seek ko previous karo", "seek ko jump karo", "peeche jao", "seek peeche karo", 
        "backward seek ko karo"
    ]:
        seek_backward()
    elif text in [
        "seek forward 10s", "forward 10 seconds", "jump forward 10s", "skip forward 10s", "advance 10 seconds", "move forward 10s", "go forward 10s", 
        "forward by 10 seconds", "10s forward", "10 seconds ahead", "10s jump forward", "10s skip forward", "forward 10 sec", "advance 10s", "10s advance", 
        "10 second aage", "10 second badhao", "10s ko aage karo", "10s ko forward karo", "seek 10s aage", "10 second forward", "seek ko 10 second aage karo", 
        "seek ko 10 second badhao", "10s ko aage badhao", "forward 10s karo", "10 second aage badhao", "10 second seek aage", "10 second jump forward", 
        "seek ko 10s aage karo", "10s aage karo"
    ]:
        seek_forward_10s()
    elif text in [
        "seek backward 10s", "backward 10 seconds", "jump backward 10s", "skip backward 10s", "rewind 10 seconds", "move backward 10s", "go backward 10s", 
        "back by 10 seconds", "10s backward", "10 seconds back", "10s jump back", "10s skip back", "backward 10 sec", "rewind 10s", "10s rewind", 
        "10 second peeche", "10 second badhao peeche", "10s ko peeche karo", "10s ko backward karo", "seek 10s peeche", "10 second backward", "seek ko 10 second peeche karo", 
        "seek ko 10 second badhao peeche", "10s ko peeche badhao", "backward 10s karo", "10 second peeche badhao", "10 second seek peeche", "10 second jump backward", 
        "seek ko 10s peeche karo", "10s peeche karo"
    ]:
        seek_backward_10s()
    elif text in [
        "seek backward frame", "backward frame", "move backward frame", "previous frame", "skip backward frame", "jump backward frame", "rewind frame", "frame back", 
        "frame rewind", "backward by frame", "frame backward", "one frame back", "frame seek backward", "frame move back", "go back frame", 
        "frame peeche", "frame peeche karo", "frame ko peeche badhao", "frame ko backward karo", "frame ko peeche karo", "seek frame peeche", "frame ko seek peeche karo", 
        "frame ko peeche badhao", "seek ko frame peeche karo", "backward frame karo", "frame ko badhao peeche", "frame ko seek karo", "seek frame karo peeche", "frame ko back karo", 
        "frame peeche le jao"
    ]:
        seek_backward_frame()
    elif text in [
        "seek forward frame", "forward frame", "move forward frame", "next frame", "skip forward frame", "jump forward frame", "advance frame", "frame forward", 
        "frame advance", "forward by frame", "frame forward move", "one frame forward", "frame seek forward", "frame move forward", "go forward frame", 
        "frame aage", "frame aage karo", "frame ko aage badhao", "frame ko forward karo", "frame ko aage karo", "seek frame aage", "frame ko seek aage karo", 
        "frame ko aage badhao", "seek ko frame aage karo", "forward frame karo", "frame ko badhao aage", "frame ko seek karo", "seek frame karo aage", "frame ko forward karo", 
        "frame aage le jao"
    ]:
        seek_forward_frame()
    elif text in [
        "seek to beginning", "start", "beginning", "go to beginning", "move to start", "jump to beginning", "skip to start", "seek start", "seek beginning", 
        "go to start", "beginning seek", "start seek", "seek home", "seek initial", "beginning move", 
        "shuru me le jao", "starting par le jao", "starting me le jao", "beginning par le jao", "shuru me", "starting ko", "beginning ko", "seek start karo", 
        "seek shuru karo", "seek shuruat karo", "seek ko shuru karo", "seek ko start karo", "seek ko shuruat karo", "seek ko initial karo", "shuru karo"
    ]:
        seek_to_beginning()
    elif text in [
        "seek to end", "end", "finish", "go to end", "move to end", "jump to end", "skip to end", "seek end", "seek finish", 
        "go to finish", "end seek", "finish seek", "seek end", "seek finish", "move to end", 
        "end par le jao", "ending par le jao", "ending me le jao", "ant par le jao", "end me", "ending ko", "ant ko", "seek end karo", 
        "seek ant karo", "seek end karo", "seek ko ant karo", "seek ko end karo", "seek ko finish karo", "seek ko ending karo", "ant karo"
    ]:
        seek_to_end()
    elif text in [
        "seek to previous chapter", "previous chapter", "move to previous chapter", "go to previous chapter", "jump to previous chapter", "skip to previous chapter", 
        "seek previous chapter", "chapter back", "chapter previous", "chapter seek", "chapter backward", "previous chapter seek", "chapter go back", 
        "chapter move back", "chapter jump back", 
        "pehla chapter", "pichla chapter", "previous chapter par le jao", "chapter peeche", "pichle chapter par le jao", "chapter ko pichla karo", "chapter peeche karo", 
        "seek pichla chapter", "seek chapter peeche", "chapter ko peeche karo", "chapter ko peeche le jao", "chapter ko pichla karo", "chapter ko previous karo", 
        "chapter peeche le jao", "pichla chapter par jaye", "chapter ko peeche karo"
    ]:
        seek_to_previous_chapter()
    elif text in [
        "seek to next chapter", "next chapter", "move to next chapter", "go to next chapter", "jump to next chapter", "skip to next chapter", 
        "seek next chapter", "chapter forward", "chapter next", "chapter seek", "chapter advance", "next chapter seek", "chapter go forward", 
        "chapter move forward", "chapter jump forward", 
        "agli chapter", "next chapter par le jao", "chapter aage", "agli chapter par le jao", "chapter ko aage karo", "chapter aage karo", 
        "seek agli chapter", "seek chapter aage", "chapter ko aage karo", "chapter ko aage le jao", "chapter ko agli karo", "chapter ko next karo", 
        "chapter aage le jao", "next chapter par jaye", "chapter ko aage karo"
    ]:
        seek_to_next_chapter()
    elif text in [
        "decrease playback speed", "slow down", "reduce speed", "lower speed", "slow speed", "decrease speed", "playback slow", "playback reduce", "playback lower", 
        "playback slow down", "reduce playback speed", "lower playback speed", "slow down playback", "decrease speed playback", "slow the playback", 
        "playback speed kam karo", "speed kam karo", "playback ko slow karo", "playback ko kam karo", "playback ko reduce karo", "speed ko kam karo", "speed ko reduce karo", 
        "playback ko slow karna", "playback ko speed slow karo", "speed kam karna", "speed kam karo playback", "speed ko kam karo playback", "speed playback kam karo", 
        "playback speed ko kam karo", "speed ko slow karo"
    ]:
        decrease_playback_speed()
    elif text in [
        "increase playback speed", "speed up", "raise speed", "increase speed", "fast speed", "speed high", "playback fast", "playback increase", "playback raise", 
        "playback speed up", "increase playback speed", "raise playback speed", "speed up playback", "increase speed playback", "fast the playback", 
        "playback speed badhao", "speed badhao", "playback ko fast karo", "playback ko tez karo", "playback ko increase karo", "speed ko badhao", "speed ko increase karo", 
        "playback ko tez karna", "playback ko speed fast karo", "speed badhaana", "speed badhao playback", "speed ko badhao playback", "speed playback badhao", 
        "playback speed ko badhao", "speed ko fast karo"
    ]:
        increase_playback_speed()
    elif text in [
        "move to next video", "next video", "go to next video", "play next video", "skip to next video", "jump to next video", "switch to next video", "advance to next video", 
        "next video play", "next video go", "move to next vid", "next vid", "jump to next vid", "skip to next vid", "advance to next vid", 
        "agli video", "next video par le jao", "video aage", "agli video par le jao", "video ko aage karo", "video aage karo", 
        "seek agli video", "seek video aage", "video ko aage karo", "video ko aage le jao", "video ko agli karo", "video ko next karo", 
        "video aage le jao", "next video par jaye", "video ko aage karo"
    ]:
        move_to_next_video()
    elif text in [
        "move to previous video", "previous video", "go to previous video", "play previous video", "skip to previous video", "jump to previous video", "switch to previous video", 
        "rewind to previous video", "previous video play", "previous video go", "move to prev vid", "prev vid", "jump to prev vid", "skip to prev vid", "rewind to prev vid", 
        "pichli video", "pichla video", "previous video par le jao", "video peeche", "pichli video par le jao", "video ko peeche karo", "video peeche karo", 
        "seek pichli video", "seek video peeche", "video ko peeche karo", "video ko peeche le jao", "video ko pichli karo", "video ko previous karo", 
        "video peeche le jao", "previous video par jaye", "video ko peeche karo"
    ]:
        move_to_previous_video()
    else:
        pass
