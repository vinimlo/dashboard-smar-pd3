<template>
  <div class="control-btn-container">
    <button class="control-btn control-btn-on" @click="sendSocketMessage('set_bomb_1_on')">ON</button>
    <button class="control-btn control-btn-off" @click="sendSocketMessage('set_bomb_1_off')">OFF</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SocketIOService from '../services/socketio.service';

export default defineComponent({
  name: 'ControlButton',
  methods: {
    sendSocketMessage(message: string): void {
      SocketIOService.emitMessage(message);
    }
  }
});
</script>

<style scoped>
.control-btn-container {
  width: 50px;
  height: 100px;
  display: block;
  border-style: solid;
  border-width: 5px;
  border-color: #283159;
  border-radius: 12px;
}

.control-btn {
  width: 100%;
  height: 50px;
  border: none;
  padding: 0;
  margin: 0;
  display: block;
  cursor: pointer;
  color: #F2F2F2;
  font-weight: 700;
}

.control-btn:active {
  background-color: #283159;
}

.control-btn-on {
  background-color: rgba(0, 0, 0, 0);
  border-radius: 6px 6px 0 0;
}

.control-btn-off {
  background-color: rgba(0, 0, 0, 0);
  border-radius: 0 0 6px 6px;
}
</style>