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
          },
          fill: {
            type: "gradient",
            gradient: {
              gradientToColors: ["#F55555", "#6078ea", "#6094ea"]
            }
          }
        },
        plotOptions: {
          radialBar: {
            startAngle: -90,
            endAngle: 90,
            track: {
              background: "#262d47",

              strokeWidth: '80%',
              margin: 3, // margin is in pixels
              dropShadow: {
                enabled: false,
                top: 2,
                left: 0,
                color: '#373737',
                opacity: 1,
                blur: 2
              }
            },
            dataLabels: {
              enabled: true,
              background: {
                enabled: true,
                foreColor: '#F2F2F2',
              },
              name: {
                show: true,
                fontSize: '16px',
                fontWeight: 600,
                color: '#FFFFFF',
              },
              value: {
                offsetY: -50,
                fontSize: '22px',
                fontWeight: 600,
                color: '#FFFFFF',
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
          type: "gradient",
          colors: [(this.variableToRead === 'temperature' ? '#f55854' : '#18e9d9')],
          opacity: 0.9,
          gradient: {
            shade: 'dark',
            type: "vertical",
            shadeIntensity: 0.95,
            gradientToColors: [(this.variableToRead === 'temperature' ? '#fccf31' : '#6078ea')],
            inverseColors: true,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100],
            colorStops: []
          }
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
  height: 225px;
  display: flex;
  align-items: center;
  background-color: rgba(38, 45, 71, 0.35);
  border-radius: 8px;
}
</style>
