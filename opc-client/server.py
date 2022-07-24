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
    # Add tank mock variables
    py_level_1 = opc_obj.add_variable(idx, "Py_Level_1", 5.00)
    py_temperature_1 = opc_obj.add_variable(idx, "Py_Temperature_1", 5.00)
    py_flow_1 = opc_obj.add_variable(idx, "Py_Flow_1", 5.00)
    py_temperature_2 = opc_obj.add_variable(idx, "Py_Temperature_2", 5.00)
    py_flow_2 = opc_obj.add_variable(idx, "Py_Flow_2", 5.00)
    # Add tank mock alarms
    py_alarm_panel = opc_obj.add_variable(idx, "Py_Alarm_Panel", True)
    py_alarm_emergency = opc_obj.add_variable(idx, "Py_Alarm_Emergency", False)
    py_alarm_low_level_1 = opc_obj.add_variable(idx, "Py_Alarm_Low_Level_1", True)
    py_alarm_high_temperature_1 = opc_obj.add_variable(idx, "Py_Alarm_High_Temperature_1", False)
    py_alarm_high_temperature_2 = opc_obj.add_variable(idx, "Py_Alarm_High_Temperature_2", False)
    # py_temperature_1.set_writable()

    server.start()

    try:
        count = 5.0
        while True:
            time.sleep(2)
            if(count < 99.5):
                py_level_1.set_value(count)
                py_temperature_1.set_value(count/2)
                py_flow_1.set_value(count/4)
                py_temperature_2.set_value(50 - count/2)
                py_flow_2.set_value(50 - count/4)
                count += 0.5
            else:
                count = 5.0
    finally:
        print("Stopping")
        server.stop()
