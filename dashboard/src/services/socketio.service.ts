import { io, Socket } from 'socket.io-client';

class SocketIOService {
  socket: Socket;
  levelValue: number;
  variableDict: Record<string, number | boolean> = {};

  constructor() {
    this.levelValue = 0;

    this.variableDict['level_1'] = 0;
    this.variableDict['temperature_1'] = 0;
    this.variableDict['flow_1'] = 0;
    this.variableDict['temperature_2'] = 0;
    this.variableDict['flow_2'] = 0;

    this.variableDict['alarm_panel'] = false;
    this.variableDict['alarm_emergency'] = false;
    this.variableDict['alarm_low_level_1'] = false;
    this.variableDict['alarm_high_temperature_1'] = false;
    this.variableDict['alarm_high_temperature_2'] = false;

    this.variableDict['bomb_1'] = false;
    this.variableDict['valve_1'] = false;
    this.variableDict['heater'] = false;

    this.socket = io(process.env.VUE_APP_SOCKET_ENDPOINT);
  }

  async setupSocketConnection(variableToRead: string): Promise<void> {
    this.socket.on(`send_${variableToRead}_value`, (data: { value: boolean | number }): void => {
      this.variableDict[variableToRead] = data.value;
      this.socket.emit(`request_${variableToRead}_value`)
    });
  }
  disconnect() {
    if (this.socket) {
      this.socket.disconnect()
    }
  }
  requestVariable(variableToRead: string): void {
    this.socket.emit(`request_${variableToRead}_value`);
  }
  emitMessage(message: string): void {
    this.socket.emit(message);
  }
}

export default new SocketIOService();