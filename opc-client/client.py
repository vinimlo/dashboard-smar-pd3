import asyncio
import sys
from asyncua import Client
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, "..")


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
    'alarm_high_temperature_2': 'ns=2;i=11',
    'bomb_1': 'ns=2;i=12',
    'valve_1': 'ns=2;i=13',
    'heater': 'ns=2;i=14'
}


async def get_variable_address(client, variable_name):
    root = client.get_root_node()
    variable_address = await root.get_child(["0:Objects", "2:Py_PD3_Objects", f"2:{variable_name}"])
    return(variable_address)


async def read_opc_variable(variable_to_read: str) -> float:
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        opc_variable = client.get_node(variable_dict[variable_to_read])
        variable_value = await opc_variable.get_value()
        return variable_value


async def set_opc_variable(variable_to_set: str, value: any) -> None:
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        opc_variable = client.get_node(variable_dict[variable_to_set])
        await opc_variable.write_value(value)


async def increase_level_value(py_bomb_1, py_level_1, py_flow_1):
    py_level_1_value = await py_level_1.get_value()
    py_bomb_1_value = await py_bomb_1.get_value()
    py_flow_1_value = await py_flow_1.get_value()

    if((py_bomb_1_value == True) and (py_level_1_value < 100)):
        value = py_level_1_value + (10 * (py_flow_1_value/100))
        await py_level_1.set_value(value)
        await py_flow_1.set_value(100 - value)
        await asyncio.sleep(1)
        await increase_level_value(py_bomb_1, py_level_1, py_flow_1)

    await py_bomb_1.set_value(False)
    await py_flow_1.set_value(0.0)


async def activate_bomb_1():
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        py_bomb_1 = client.get_node(variable_dict['bomb_1'])
        py_level_1 = client.get_node(variable_dict['level_1'])
        py_flow_1 = client.get_node(variable_dict['flow_1'])

        await py_bomb_1.set_value(True)
        await py_flow_1.set_value(100.0)

        await increase_level_value(py_bomb_1, py_level_1, py_flow_1)


async def decrease_level_value(py_valve_1, py_level_1, py_flow_1):
    py_level_1_value = await py_level_1.get_value()
    py_valve_1_value = await py_valve_1.get_value()
    py_flow_1_value = await py_flow_1.get_value()

    if((py_valve_1_value == True) and (py_level_1_value > 0)):
        value = py_level_1_value - (10 * (py_flow_1_value/100))
        await py_level_1.set_value(value)
        await py_flow_1.set_value(value)
        await asyncio.sleep(1)
        await decrease_level_value(py_valve_1, py_level_1, py_flow_1)

    await py_valve_1.set_value(False)
    await py_flow_1.set_value(0.0)


async def activate_valve_1():
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        py_valve_1 = client.get_node(variable_dict['valve_1'])
        py_level_1 = client.get_node(variable_dict['level_1'])
        py_flow_1 = client.get_node(variable_dict['flow_1'])

        await py_valve_1.set_value(True)
        await py_flow_1.set_value(100.0)

        await decrease_level_value(py_valve_1, py_level_1, py_flow_1)


async def increase_temperature_value(py_heater, py_temperature_1, py_alarm_low_level_1):
    py_heater_value = await py_heater.get_value()
    py_temperature_1_value = await py_temperature_1.get_value()
    py_alarm_low_level_1_value = await py_alarm_low_level_1.get_value()

    if((py_heater_value == True) and (py_temperature_1_value < 50) and (py_alarm_low_level_1_value == False)):
        value = py_temperature_1_value + 2
        await py_temperature_1.set_value(value)
        await asyncio.sleep(1)
        await increase_temperature_value(py_heater, py_temperature_1, py_alarm_low_level_1)

    await py_heater.set_value(False)


async def activate_heater():
    client = Client(os.getenv('OPC_SERVER_URI'))
    async with client:
        py_heater = client.get_node(variable_dict['heater'])
        py_temperature_1 = client.get_node(variable_dict['temperature_1'])
        py_alarm_low_level_1 = client.get_node(variable_dict['alarm_low_level_1'])

        await py_heater.set_value(True)

        await increase_temperature_value(py_heater, py_temperature_1, py_alarm_low_level_1)
