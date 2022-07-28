<template>
  <div class="control-btn-container">
    <p>{{ controlBtnName }}</p>
    <div class="control-btn-wrapper">
      <button class="control-btn control-btn-on" @click="sendSocketMessage(`set_${instrument}_on`)"
        :class="isInstrumentActive">ON</button>
      <button class="control-btn control-btn-off" @click="sendSocketMessage(`set_${instrument}_off`)"
        :class="isInstrumentActive">OFF</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SocketIOService from '../services/socketio.service';

export default defineComponent({
  name: 'ControlButton',
  data() {
    return {
      instrumentValue: 0 as boolean | number
    }
  },
  computed: {
    isInstrumentActive() {
      return this.instrumentValue ? 'is-on' : 'is-off'
    }
  },
  props: {
    instrument: {
      type: String,
      default: ''
    },
    controlBtnName: {
      type: String,
      default: ''
    }
  },
  created() {
    SocketIOService.setupSocketConnection(this.instrument);
    SocketIOService.requestVariable(this.instrument);
  },
  mounted() {
    this.getVariableValue();
  },
  beforeUnmount() {
    SocketIOService.disconnect();
  },
  methods: {
    sendSocketMessage(message: string): void {
      SocketIOService.emitMessage(message);
    },
    getVariableValue() {
      setInterval(() => {
        this.instrumentValue = SocketIOService.variableDict[this.instrument];
      }, 500);
    }
  }
});
</script>

<style scoped>
.control-btn-container {
  text-align: center;
}

.control-btn-container p {
  color: #F2F2F2;
  font-weight: 500;
  font-size: 1.3rem;
  margin: 0;
  padding: 10px 0;
}

.control-btn-wrapper {
  margin: 0 auto;
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

.control-btn.control-btn-on.is-on {
  background-color: #00C853;
}

.control-btn.control-btn-off.is-off {
  background-color: #D32F2F;
}
</style>