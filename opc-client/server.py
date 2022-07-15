from xmlrpc.client import Boolean
from opcua import ua, Server
import sys
import time
from random import randint

sys.path.insert(0, "..")

if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")
    uri = "vinimlo"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    myobj = objects.add_object(idx, "PyOPCObject")
    py_temperature = myobj.add_variable(idx, "Py_Temperature", 0)
    py_level = myobj.add_variable(idx, "Py_Level", 15.00)
    py_alarm = myobj.add_variable(idx, "Py_Alarm", True)
    py_temperature.set_writable()
    py_level.set_writable()

    server.start()

    try:
        count = 15.0
        while True:
            time.sleep(5)
            if(count < 20.0):
                py_level.set_value(count)
                count += 0.2
            else:
                count = 15.0
            py_temperature.set_value(26.72)
    finally:
        print("Stopping")
        server.stop()
