from aiohttp import web
import socketio
from client import read_opc_variables

_socket = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
_socket.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@_socket.event
def connect(sid, environ):
    print("connect ", sid)


@_socket.event
def disconnect(sid):
    print('disconnect ', sid)


@_socket.event
async def request_level_value(sid):
    level_value = await read_opc_variables()
    await _socket.emit('send_level_value', {'value': round(level_value, 1)}, room=sid)


app.router.add_get('/', index)


if __name__ == "__main__":
    web.run_app(app)
