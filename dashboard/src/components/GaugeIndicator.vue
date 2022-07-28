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
import LineChart from './LineChart.vue';

export default defineComponent({
  name: 'GaugeIndicator',
  props: {
    variableToRead: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      variableValue: 0 as boolean | number,
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
                formatter: (value: number) => {
                  return value + ` ${this.measurementUnit}`
                }
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
          colors: [(this.variableToRead.split('_')[0] === 'temperature' ? '#f55854' : this.variableToRead.split('_')[0] === 'level' ? '#18e9d9' : '#6590e8')],
          opacity: 0.9,
          gradient: {
            shade: 'dark',
            type: "vertical",
            shadeIntensity: 0.95,
            gradientToColors: [(this.variableToRead.split('_')[0] === 'temperature' ? '#fccf31' : this.variableToRead.split('_')[0] === 'level' ? '#6078ea' : '#f02fc2')],
            inverseColors: true,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100],
            colorStops: []
          }
        },
        labels: [this.variableToRead.split('_').join(' ').toUpperCase()],
      },
    }
  },
  computed: {
    measurementUnit() {
      return this.variableToRead.split('_')[0] === 'temperature' ? ' ºC' : this.variableToRead.split('_')[0] === 'level' ? ' %' : 'L/h'
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
        if(this.variableToRead === 'level_1') {
          (this.$root?.$refs['lineChart'] as typeof LineChart).appendLevelValue(this.variableValue);
        } else if(this.variableToRead === 'flow_1') {
          (this.$root?.$refs['lineChart'] as typeof LineChart).appendFlowValue(this.variableValue);
        }
      }, 500);
    }
  }
});
</script>

<style scoped>
.gauge-item {
  width: 350px;
  height: 180px;
  display: flex;
  align-items: center;
  background-color: rgba(38, 45, 71, 0.35);
  border-radius: 8px;
}
</style>
