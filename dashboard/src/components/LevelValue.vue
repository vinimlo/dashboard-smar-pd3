<template>
  <div id="chart">
    <apexchart type="radialBar" :options="chartOptions" :series="[level_value]"></apexchart>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SocketIOService from '../services/socketio.service';

export default defineComponent({
  name: 'LevelValue',
  props: {
    timeInSeconds: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      level_value: 0,
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
                show: false
              },
              value: {
                offsetY: -2,
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
        labels: ['Average Results'],
      },
    }
  },
  created() {
    SocketIOService.setupSocketConnection();
    SocketIOService.requestLevel();
  },
  mounted() {
    this.getLevelValue();
  },
  beforeUnmount() {
    SocketIOService.disconnect();
  },
  methods: {
    getLevelValue() {
      setInterval(() => {
        this.level_value = SocketIOService.level_value;
      }, 1000);
    }
  }
});
</script>

<style scoped>
</style>
