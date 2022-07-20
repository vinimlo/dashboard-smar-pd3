import { io, Socket } from 'socket.io-client';

class SocketIOService {
  socket: Socket;
  level_value: number;
  
  constructor() {
    this.level_value = 0;
    this.socket = io('http://localhost:4113');
  }

  async setupSocketConnection() {
    this.socket.on('send_level_value', (data: {value: number}) => {
      this.level_value = data.value;
      console.log(data.value);
      this.socket.emit('request_level_value')
    });
  }
  disconnect() {
    if(this.socket) {
      this.socket.disconnect()
    }
  }
  requestLevel() {
    this.socket.emit('request_level_value');
  }
  test() {
    return this.level_value;
  }
}

export default new SocketIOService();