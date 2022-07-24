import sys
from asyncua import Client
import csv
from datetime import datetime

sys.path.insert(0, "..")


async def read_opc_variable(variable_to_read: str) -> float:
    client = Client("opc.tcp://localhost:4840")
    async with client:
        # root = client.get_root_node()
        # obj = await root.get_child(["0:Objects", "2:PyOPCObject"])
        # py_level_1 = await root.get_child(["0:Objects", "2:PyOPCObject", "2:Py_Level_1"])
        # print("Alarm Panel is: ", py_alarm_panel)

        variable_dict: dict = {
            'level_1': 'ns=2;i=2',
            'temperature_1': 'ns=2;i=3',
            'flow_1': 'ns=2;i=4',
            'temperature_2': 'ns=2;i=5',
            'flow_2': 'ns=2;i=6',
            'alarm_panel': 'ns=2;i=7',
            'alarm_emergency': 'ns=2;i=8',
            'alarm_low_level_1': 'ns=2;i=9',
            'alarm_high_temperature_1': 'ns=2;i=10',
            'alarm_high_temperature_2': 'ns=2;i=11'
        }

        variable_value = await client.get_node(variable_dict[variable_to_read]).get_value()
        return variable_value
