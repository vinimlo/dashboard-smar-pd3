import { io, Socket } from 'socket.io-client';

class SocketIOService {
  socket: Socket;
  levelValue: number;
  variableDict: Record<string, number> = {};
  
  constructor() {
    this.levelValue = 0;
    this.variableDict['level'] = 0;
    this.variableDict['temperature'] = 0;
    this.variableDict['flow'] = 0;
    this.socket = io('http://localhost:4113');
  }

  async setupSocketConnection(variableToRead: string): Promise<void> {
    this.socket.on(`send_${variableToRead}_value`, (data: {value: number}) => {
      this.levelValue = data.value;
      this.variableDict[variableToRead] = data.value;
      console.log(this.variableDict[variableToRead]);
      this.socket.emit(`request_${variableToRead}_value`)
    });
  }
  disconnect() {
    if(this.socket) {
      this.socket.disconnect()
    }
  }
  requestVariable(variableToRead: string): void {
    this.socket.emit(`request_${variableToRead}_value`);
  }
}

export default new SocketIOService();