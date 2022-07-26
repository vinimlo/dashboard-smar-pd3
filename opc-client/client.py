import sys
from asyncua import Client
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, "..")


async def read_opc_variable(variable_to_read: str) -> float:
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        # root = client.get_root_node()
        # obj = await root.get_child(["0:Objects", "2:Py_PD3_Objects"])
        # py_level_1 = await root.get_child(["0:Objects", "2:Py_PD3_Objects", "2:Py_Level_1"])
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

async def set_opc_variable(variable_to_set: str, value: any) -> None:
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        variable_dict: dict = {
            'py_bomb_1': 'ns=2;i=12'
        }

        await client.get_node(variable_dict[variable_to_set]).write_value(value)