from Automation.Automation_Brain import Auto_main_brain,clear_file
from BrokenLeaf_STT import listen
import threading
from DATA.DLG_Data import online_dlg,offline_dlg
import random
from Time_Operations.brain import input_manage


ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text:
                Auto_main_brain(output_text)
            elif output_text.startswith("Tell me"):
                input_manage(output_text)
        else:
            pass

def Vox():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
