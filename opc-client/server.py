import sys
import os
import time

from dotenv import load_dotenv
from opc_server import OpcServer

load_dotenv()

_server = OpcServer(os.getenv("OPC_SERVER_URI"))

sys.path.insert(0, "..")

if __name__ == "__main__":
    _server.server.start()
    _server.configure_server()

    try:
        while True:
            py_level_1_value = _server.py_level_1.get_value()
            py_temperature_1_value = _server.py_temperature_1.get_value()
            py_flow_1_value = _server.py_flow_1.get_value()

            _server.py_alarm_low_level_1.set_value(True) if py_level_1_value < 50 else _server.py_alarm_low_level_1.set_value(False)

            _server.py_level_1.set_value(0) if py_level_1_value < 0 else _server.py_level_1.set_value(py_level_1_value)

            _server.py_flow_1.set_value(0) if py_flow_1_value < 0 else _server.py_flow_1.set_value(py_flow_1_value)

            _server.py_temperature_1.set_value(py_temperature_1_value-0.0006) if py_temperature_1_value > 0 else _server.py_temperature_1.set_value(py_temperature_1_value)
            time.sleep(0.1)
    finally:
        print("Stopping")
        _server.server.stop()
