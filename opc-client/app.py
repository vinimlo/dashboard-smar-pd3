import asyncio
from aiohttp import web
import socketio
from client import read_opc_variable

_socket = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
_socket.attach(app)


@_socket.event
def connect(sid, environ):
    _socket.enter_room(sid=sid, room='level_1')
    _socket.enter_room(sid=sid, room='temperature_1')
    _socket.enter_room(sid=sid, room='flow_1')
    _socket.enter_room(sid=sid, room='temperature_2')
    _socket.enter_room(sid=sid, room='flow_2')

    _socket.enter_room(sid=sid, room='alarm_panel')
    _socket.enter_room(sid=sid, room='alarm_emergency')
    _socket.enter_room(sid=sid, room='alarm_low_level_1')
    _socket.enter_room(sid=sid, room='alarm_high_temperature_1')
    _socket.enter_room(sid=sid, room='alarm_high_temperature_2')
    print("connect ", sid)


@_socket.event
def disconnect(sid):
    print('disconnect ', sid)


@_socket.event
async def request_level_1_value(sid):
    level_value = await read_opc_variable('level_1')
    await asyncio.sleep(2)
    await _socket.emit('send_level_1_value', {'value': round(level_value, 1)}, room='level_1')


@_socket.event
async def request_temperature_1_value(sid):
    temperature_value = await read_opc_variable('temperature_1')
    await asyncio.sleep(2)
    await _socket.emit('send_temperature_1_value', {'value': round(temperature_value, 1)}, room='temperature_1')


@_socket.event
async def request_flow_1_value(sid):
    flow_value = await read_opc_variable('flow_1')
    await asyncio.sleep(2)
    await _socket.emit('send_flow_1_value', {'value': round(flow_value, 1)}, room='flow_1')


@_socket.event
async def request_temperature_2_value(sid):
    temperature_value = await read_opc_variable('temperature_2')
    await asyncio.sleep(2)
    await _socket.emit('send_temperature_2_value', {'value': round(temperature_value, 1)}, room='temperature_2')


@_socket.event
async def request_flow_2_value(sid):
    flow_value = await read_opc_variable('flow_2')
    await asyncio.sleep(2)
    await _socket.emit('send_flow_2_value', {'value': round(flow_value, 1)}, room='flow_2')


@_socket.event
async def request_alarm_panel_value(sid):
    alarm_value = await read_opc_variable('alarm_panel')
    await asyncio.sleep(2)
    await _socket.emit('send_alarm_panel_value', {'value': alarm_value}, room='alarm_panel')


@_socket.event
async def request_alarm_emergency_value(sid):
    alarm_value = await read_opc_variable('alarm_emergency')
    await asyncio.sleep(2)
    await _socket.emit('send_alarm_emergency_value', {'value': alarm_value}, room='alarm_emergency')


@_socket.event
async def request_alarm_low_level_1_value(sid):
    alarm_value = await read_opc_variable('alarm_low_level_1')
    await asyncio.sleep(2)
    await _socket.emit('send_alarm_low_level_1_value', {'value': alarm_value}, room='alarm_low_level_1')


@_socket.event
async def request_alarm_high_temperature_1_value(sid):
    alarm_value = await read_opc_variable('alarm_high_temperature_1')
    await asyncio.sleep(2)
    await _socket.emit('send_alarm_high_temperature_1_value', {'value': alarm_value}, room='alarm_high_temperature_1')


@_socket.event
async def request_alarm_high_temperature_2_value(sid):
    alarm_value = await read_opc_variable('alarm_high_temperature_2')
    await asyncio.sleep(2)
    await _socket.emit('send_alarm_high_temperature_2_value', {'value': alarm_value}, room='alarm_high_temperature_2')

if __name__ == "__main__":
    web.run_app(app, port="4113")
