import threading
from Internet_checker import is_Online
from Alert import Alert
from DATA.DLG_Data import online_dlg, offline_dlg
import random
from co_brain import Vox
from BrokenLeaf_TTS import speak
from Time_Operations.brain import input_manage
from Time_Operations.throw_alert import check_schedule
from Automation.Battery import check_plug

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def wish():
        t1 = threading.Thread(target=speak,args=(ran_online_dlg,))
        t2 = threading.Thread(target=Alert,args=(ran_online_dlg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def Main():
    if is_Online():
        wish()
        t3 = threading.Thread(target=check_schedule)
        t4 = threading.Thread(target=check_plug)
        t5 = threading.Thread(target=Vox)
        t3.start()
        t4.start()
        t5.start()
        t3.join()
        t4.join()
        t5.join()
    else:
        Alert(ran_offline_dlg)

Main()