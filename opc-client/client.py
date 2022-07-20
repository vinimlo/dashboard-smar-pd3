import sys
from asyncua import Client
import csv
from datetime import datetime

sys.path.insert(0, "..")


async def read_opc_variables():
    client = Client("opc.tcp://localhost:4840")
    async with client:
        root = client.get_root_node()

        obj = await root.get_child(["0:Objects", "2:PyOPCObject"])
        py_temperature = await root.get_child(
            ["0:Objects", "2:PyOPCObject", "2:Py_Temperature"])
        py_level = await root.get_child(["0:Objects", "2:PyOPCObject", "2:Py_Level"])
        py_alarm = await root.get_child(["0:Objects", "2:PyOPCObject", "2:Py_Alarm"])
        # print("My object is: ", obj)
        # print("Py_Temperature is: ", py_temperature)
        # print("Py_Level is: ", py_level)
        # print("Py_Alarm is: ", py_alarm)
        # level_handler = LevelHandler()
        # level_sub = await client.create_subscription(500, level_handler)
        # level_handle = await level_sub.subscribe_data_change(py_level)

        level_value = await client.get_node("ns=2;i=3").get_value()

        return level_value
