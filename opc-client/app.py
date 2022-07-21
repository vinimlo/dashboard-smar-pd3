import asyncio
from aiohttp import web
import socketio
from client import read_opc_variable

_socket = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
_socket.attach(app)


@_socket.event
def connect(sid, environ):
    _socket.enter_room(sid=sid, room='level')
    _socket.enter_room(sid=sid, room='temperature')
    _socket.enter_room(sid=sid, room='flow')
    print("connect ", sid)


@_socket.event
def disconnect(sid):
    print('disconnect ', sid)


@_socket.event
async def request_level_value(sid):
    level_value = await read_opc_variable('level')
    await asyncio.sleep(2)
    await _socket.emit('send_level_value', {'value': round(level_value, 1)}, room='level')


@_socket.event
async def request_temperature_value(sid):
    temperature_value = await read_opc_variable('temperature')
    await asyncio.sleep(2)
    await _socket.emit('send_temperature_value', {'value': round(temperature_value, 1)}, room='temperature')


@_socket.event
async def request_flow_value(sid):
    flow_value = await read_opc_variable('flow')
    await asyncio.sleep(2)
    await _socket.emit('send_flow_value', {'value': round(flow_value, 1)}, room='flow')

if __name__ == "__main__":
    web.run_app(app, port="4113")
