<template>
  <div class="gauge-item">
    <div id="chart">
      <apexchart type="radialBar" :options="chartOptions" :series="[variableValue]"></apexchart>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SocketIOService from '../services/socketio.service';

export default defineComponent({
  name: 'VariableGauge',
  props: {
    variableToRead: {
      type: String,
      default: 'level'
    }
  },
  data() {
    return {
      variableValue: 0,
      chartOptions: {
        chart: {
          type: 'radialBar',
          offsetY: -20,
          sparkline: {
            enabled: true
          }
        },
        plotOptions: {
          radialBar: {
            startAngle: -90,
            endAngle: 90,
            track: {
              background: "#e7e7e7",
              strokeWidth: '97%',
              margin: 5, // margin is in pixels
              dropShadow: {
                enabled: true,
                top: 2,
                left: 0,
                color: '#999',
                opacity: 1,
                blur: 2
              }
            },
            dataLabels: {
              name: {
                show: true,
              },
              value: {
                offsetY: -50,
                fontSize: '22px'
              }
            }
          }
        },
        grid: {
          padding: {
            top: -10
          }
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'light',
            shadeIntensity: 0.4,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 50, 53, 91]
          },
        },
        labels: [this.variableToRead.toUpperCase()],
      },
    }
  },
  created() {
    SocketIOService.setupSocketConnection(this.variableToRead);
    SocketIOService.requestVariable(this.variableToRead);
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
        this.variableValue = SocketIOService.variableDict[this.variableToRead];
      }, 1000);
    }
  }
});
</script>

<style scoped>
.gauge-item {
  width: 400px;
  height: auto;
}
</style>
