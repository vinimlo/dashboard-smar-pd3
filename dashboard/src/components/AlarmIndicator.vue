<template>
  <div class="alarm-wrapper">
    <h4>{{ alarmName }}</h4>
    <div class="alarm-item" :class="isAlarmOn">
      <p>{{ isAlarmOn.toUpperCase() }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SocketIOService from '../services/socketio.service';

export default defineComponent({
  name: 'AlarmIndicator',
  props: {
    alarmToRead: {
      type: String,
      default: ''
    },
    alarmName: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      alarmValue: false as boolean | number
    }
  },
  computed: {
    isAlarmOn() {
      return this.alarmValue ? 'on' : 'off'
    }
  },
  created() {
    SocketIOService.setupSocketConnection(this.alarmToRead);
    SocketIOService.requestVariable(this.alarmToRead);
  },
  mounted() {
    this.getVariableValue();
  },
  beforeUnmount() {
    SocketIOService.disconnect();
  },
  methods: {
    getVariableValue() {
      setInterval(() => {
        this.alarmValue = SocketIOService.variableDict[this.alarmToRead];
      }, 1000);
    }
  }
});
</script>

<style scoped>
h4 {
  width: 80%;
  min-height: 50px;
  text-align: center;
  color: #F2F2F2;
  font-weight: 600;
  font-size: 1rem;
}

.alarm-wrapper {
  width: 200px;
  height: 220px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(38, 45, 71, 0.35);
  border-radius: 8px;
}

.alarm-item.off {
  --alarm-bg: #1b213b;
  --alarm-text: #F2F2F2;
}

.alarm-item.on {
  --alarm-bg: #F2F2F2;
  --alarm-text: #1b213b;
}

.alarm-item {
  width: 70px;
  height: 70px;
  border: 8px solid #F2F2F2;
  background-color: var(--alarm-bg);
  border-radius: 50%;
  display: table;
}

.alarm-item p {
  text-align: center;
  vertical-align: middle;
  font-weight: 900;
  color: var(--alarm-text);
  display: table-cell;
}
</style>