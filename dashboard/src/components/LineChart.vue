<template>
  <div id="chart">
    <apexchart type="line" height="350" ref="chart" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Chart from 'vue3-apexcharts';

export default defineComponent({
  name: 'LineChart',
  data() {
    return {
      levelItems: [] as Array<number>,
      flowItems: [] as Array<number>,
      series: [{
        name: "Level Value",
        data: this.levelItems
      },
      {
        name: "Flow Value",
        data: this.flowItems
      }],
      chartOptions: {
        chart: {
          height: 350,
          type: 'line',
          stacked: false,
          zoom: {
            enabled: false
          },
          animations: {
            enabled: true,
            easing: "linear",
            dynamicAnimation: {
              speed: 1000
            }
          },
          dropShadow: {
            enabled: true,
            opacity: 0.3,
            blur: 5,
            left: -7,
            top: 22
          },
        },
        dataLabels: {
          enabled: false
        },
        title: {
          text: 'Level x Flow Graphic',
          align: 'center',
          style: {
            fontSize: '16px',
            fontWeight: 'bold',
            color: '#F2F2F2'
          }
        },
        stroke: {
          curve: "smooth",
          width: 5
        },
        grid: {
          row: {
            colors: ['#1f253e']
          },
          column: {
            colors: ['#1f253e']
          },
          padding: {
            left: 0,
            right: 0
          }
        },
        markers: {
          size: 0,
          hover: {
            size: 0
          }
        },
        xaxis: {
          categories: [],
          labels: {
            style: {
              colors: "#F2F2F2"
            }
          }
        },
        yaxis: {
          type: 'numeric',
          axisTicks: {
            show: true
          },
          axisBorder: {
            show: true,
            color: "#F2F2F2"
          },
          labels: {
            style: {
              colors: "#F2F2F2"
            }
          }
        },
        toolbar: {
          show: false
        },
        legend: {
          show: true,
          floating: false,
          fontSize: '16px',
          horizontalAlign: "center",
          onItemClick: {
            toggleDataSeries: false
          },
          position: "bottom",
          labels: {
            colors: '#F2F2F2'
          }
        }
      },
    }
  },
  mounted() {
    this.updateChart();
  },
  methods: {
    appendLevelValue(levelValue: number) {
      if (this.levelItems.length < 50) {
        this.levelItems.push(levelValue);
      } else {
        this.levelItems.shift();
      }

      // this.updateChart();
    },
    appendFlowValue(flowValue: number) {
      if (this.flowItems.length < 50) {
        this.flowItems.push(flowValue);
      } else {
        this.flowItems.shift();
      }

      // this.updateChart();
    },
    updateChart() {
      setInterval(() => {
        (this.$refs.chart as typeof Chart).updateSeries([
          {
            data: this.levelItems
          },
          {
            data: this.flowItems
          }], false, true);
      }, 1000);
    }
  }

});
</script>

<style>
</style>