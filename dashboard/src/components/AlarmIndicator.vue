<template>
  <div class="alarm-wrapper" :class="isEmergency || isPanel">
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
      default: '',
      required: true
    },
    alarmName: {
      type: String,
      default: '',
      required: true
    }
  },
  data() {
    return {
      alarmValue: false as boolean | number
    }
  },
  computed: {
    isAlarmOn(): string {
      return this.alarmValue ? 'on' : 'off'
    },
    isEmergency(): string {
      return this.alarmToRead.split('_')[1] === 'emergency' ? 'emergency-alarm' : ''
    },
    isPanel(): string {
      return this.alarmToRead.split('_')[1] === 'panel' ? 'panel-alarm' : ''
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
      }, 500);
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

@keyframes flash-normal-alarm {
  10% {
    background-color: var(--alarm-text);
  }

  30% {
    background-color: var(--alarm-bg);
  }

  50% {
    background-color: var(--alarm-text);
  }

  70% {
    background-color: var(--alarm-bg);
  }

  90% {
    background-color: var(--alarm-text);
  }

  90% {
    background-color: var(--alarm-bg);
  }
}

@keyframes flash-emergency-alarm {
  10% {
    background-color: #C62828;
  }

  25% {
    background-color: var(--alarm-text);
  }

  40% {
    background-color: #C62828;
  }

  55% {
    background-color: var(--alarm-text);
  }

  70% {
    background-color: #C62828;
  }

  85% {
    background-color: var(--alarm-text);
  }

  100% {
    background-color: #C62828;
  }
}

.alarm-item.off {
  --alarm-bg: #1b213b;
  --alarm-text: rgba(200, 200, 200, 1);
}

.alarm-item.on {
  --alarm-bg: #d32f2f;
  --alarm-text: #1b213b;
  animation-name: flash-normal-alarm;
  animation-duration: 1s;
  border: 8px solid #d32f2f;
}

.alarm-item {
  width: 70px;
  height: 70px;
  border: 8px solid rgba(200, 200, 200, 1);
  background-color: var(--alarm-bg);
  border-radius: 50%;
  display: table;
  transition: background-color;
  transition-duration: 1s;
  transition-timing-function: ease-in-out;
}

.alarm-item p {
  text-align: center;
  vertical-align: middle;
  font-weight: 900;
  color: var(--alarm-text);
  display: table-cell;
}

.emergency-alarm .alarm-item {
  border-color: #C62828;
}

.emergency-alarm .alarm-item.on {
  background-color: #C62828;
  animation-name: flash-emergency-alarm;
  animation-duration: 1.5s;
}

.panel-alarm {}
</style>