import os
from winotify import Notification, audio

def Alert(Text):
    icon_path = r"E:\A.i\VOX\Logo.png"

    toast = Notification(
        app_id="💀 V.O.X 💀",
        title=Text,
        icon=icon_path,
        duration="short",
    )

    toast.set_audio(audio.Default, loop=False)

    toast.show()
