import asyncio
from aiohttp import web
import socketio
from client import read_opc_variables

_socket = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
_socket.attach(app)


@_socket.event
def connect(sid, environ):
    _socket.enter_room(sid=sid, room='level')
    print("connect ", sid)


@_socket.event
def disconnect(sid):
    print('disconnect ', sid)


@_socket.event
async def request_level_value(sid):
    level_value = await read_opc_variables()
    await asyncio.sleep(1)
    await _socket.emit('send_level_value', {'value': round(level_value, 1)}, room='level')


if __name__ == "__main__":
    web.run_app(app, port="4113")
