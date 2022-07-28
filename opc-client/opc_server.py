from opcua import Server


class OpcServer:
    def __init__(self, opc_endpoint):
        self.__server = Server()
        self.__server.set_endpoint(opc_endpoint)
        self.__idx = self.__server.register_namespace("dashboard-smar-pd3")
        self.__objects = self.__server.get_objects_node()

    def configure_server(self):
        self.opc_obj = self.__objects.add_object(self.__idx, "Py_PD3_Objects")

        # Add tank mock variables
        self.py_level_1 = self.add_writable_variable("Py_Level_1", 0.00)
        self.py_temperature_1 = self.add_writable_variable(
            "Py_Temperature_1", 15.00)
        self.py_flow_1 = self.add_writable_variable("Py_Flow_1", 0.00)
        self.py_temperature_2 = self.add_writable_variable(
            "Py_Temperature_2", 10.00)
        self.py_flow_2 = self.add_writable_variable("Py_Flow_2", 0.00)

        # Add tank mock alarms
        self.py_alarm_panel = self.add_writable_variable(
            "Py_Alarm_Panel", False)
        self.py_alarm_emergency = self.add_writable_variable(
            "Py_Alarm_Emergency", False)
        self.py_alarm_low_level_1 = self.add_writable_variable(
            "Py_Alarm_Low_Level_1", False)
        self.py_alarm_high_temperature_1 = self.add_writable_variable(
            "Py_Alarm_High_Temperature_1", False)
        self.py_alarm_high_temperature_2 = self.add_writable_variable(
            "Py_Alarm_High_Temperature_2", False)

        self.py_bomb_1 = self.add_writable_variable(
            "Py_Bomb_1", False)
        self.py_valve_1 = self.add_writable_variable(
            "Py_Valve_1", False)
        self.py_heater = self.add_writable_variable(
            "Py_Heater", False)

    def add_read_only_variable(self, variable_name, value):
        variable = self.opc_obj.add_variable(
            self.__idx, variable_name, value)
        variable.set_read_only()
        return variable

    def add_writable_variable(self, variable_name, value):
        variable = self.opc_obj.add_variable(
            self.__idx, variable_name, value)
        variable.set_writable()
        return variable

    @property
    def server(self):
        return self.__server