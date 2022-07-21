from xmlrpc.client import Boolean
from opcua import ua, Server
import sys
import time
from random import randint

sys.path.insert(0, "..")

if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")
    uri = "projetos-automacao"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    opc_obj = objects.add_object(idx, "PyOPCObject")
    # py_temperature = opc_obj.add_variable(idx, "Py_Temperature", 0)
    py_level = opc_obj.add_variable(idx, "Py_Level", 5.00)
    py_temperature = opc_obj.add_variable(idx, "Py_Temperature", 5.00)
    py_flow = opc_obj.add_variable(idx, "Py_Flow", 5.00)
    py_alarm = opc_obj.add_variable(idx, "Py_Alarm", True)
    # py_temperature.set_writable()
    # py_level.set_writable()

    server.start()

    try:
        count = 5.0
        while True:
            time.sleep(2)
            if(count < 99.5):
                py_level.set_value(count)
                py_temperature.set_value(count/2)
                py_flow.set_value(count/4)
                count += 0.5
            else:
                count = 5.0
    finally:
        print("Stopping")
        server.stop()
