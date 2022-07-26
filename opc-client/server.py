from dotenv import load_dotenv
from tkinter import Label, Frame, Tk, PhotoImage, ttk

from opc_server import OpcServer

import os
import sys
import time

load_dotenv()
sys.path.insert(0, "..")

opc_server = OpcServer(os.getenv("OPC_SERVER_URI"))

tk = Tk()
main_frame = Frame(tk)
main_frame.pack()
# test = PhotoImage(file="./test.png")
# btn = Label(main_frame, image=test)
# btn.bind(on_click)


def increase_level_value():
    if(opc_server.py_bomb_1.get_value() and (opc_server.py_level < 99)):
        opc_server.increase_value(2)
        time.sleep(1)
        increase_level_value()
    opc_server.py_bomb_1.set_value(False)

def activate_bomb_1():
    opc_server.py_bomb_1.set_value(True)
    increase_level_value()    


ttk.Button(main_frame, text="Acionar bomba 1",
           command=activate_bomb_1).pack(pady=10)

if __name__ == "__main__":
    opc_server.configure_server()
    opc_server.server.start()

    try:
        tk.mainloop()
    #     count = 5.0
    #     while True:
    #         time.sleep(2)
    #         if(count < 99.5):
    #             py_level_1.set_value(count)
    #             py_temperature_1.set_value(count/2)
    #             py_flow_1.set_value(count/4)
    #             py_temperature_2.set_value(50 - count/2)
    #             py_flow_2.set_value(50 - count/4)
    #             count += 0.5
    #         else:
    #             count = 5.0
    finally:
        print("Stopping")
        opc_server.server.stop()
