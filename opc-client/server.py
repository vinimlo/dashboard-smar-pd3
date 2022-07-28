import sys
import os
import time

from dotenv import load_dotenv
from opc_server import OpcServer

load_dotenv()

_server = OpcServer(os.getenv("OPC_SERVER_URI"))

sys.path.insert(0, "..")


def drain_water(server):
    py_level_1_value = server.py_level_1.get_value()
    py_flow_2_value = server.py_flow_2.get_value()
    DRAIN_CONSTANT = 0.05
    drained_value = py_level_1_value - DRAIN_CONSTANT

    server.py_flow_2.set_value(20.0)
    server.py_level_1.set_value(drained_value)


if __name__ == "__main__":
    _server.server.start()
    _server.configure_server()

    try:
        while True:
            py_level_1_value = _server.py_level_1.get_value()
            py_temperature_1_value = _server.py_temperature_1.get_value()
            py_flow_1_value = _server.py_flow_1.get_value()
            py_temperature_2_value = _server.py_temperature_2.get_value()

            _server.py_alarm_low_level_1.set_value(
                True) if py_level_1_value < 50 else _server.py_alarm_low_level_1.set_value(False)

            _server.py_level_1.set_value(
                0) if py_level_1_value < 0 else _server.py_level_1.set_value(py_level_1_value)

            if py_level_1_value > 80:
                drain_water(_server)
                _server.py_temperature_2.set_value(py_temperature_1_value)
            else:
                _server.py_flow_2.set_value(0.0)

            _server.py_flow_1.set_value(
                0) if py_flow_1_value < 0 else _server.py_flow_1.set_value(py_flow_1_value)

            _server.py_temperature_1.set_value(
                py_temperature_1_value - 0.0006) if py_temperature_1_value > 25 else _server.py_temperature_1.set_value(py_temperature_1_value)

            _server.py_alarm_high_temperature_1.set_value(
                True) if py_temperature_1_value > 50 else _server.py_alarm_high_temperature_1.set_value(False)

            _server.py_alarm_high_temperature_2.set_value(
                True) if py_temperature_2_value > 50 else _server.py_alarm_high_temperature_2.set_value(False)
            time.sleep(0.1)
    finally:
        print("Stopping")
        _server.server.stop()
