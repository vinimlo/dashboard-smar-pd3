<template>
  <section id="app-container">
    <div id="left-side">
      <GaugeContainer :variableItems="['temperature_1', 'level_1', 'flow_1']">
        <!-- <h3>Tank 1</h3> -->
      </GaugeContainer>
      <GaugeContainer :variableItems="['temperature_2', 'flow_2']">
        <!-- <h3>Tank 2</h3> -->
      </GaugeContainer>
      <LineChart ref="lineChart"></LineChart>
      </div>
    <div id="right-side">
      <ControlPanel />
      <AlarmContainer
        :alarmItems="['alarm_low_level_1', 'alarm_high_temperature_1', 'alarm_high_temperature_2']">
        <!-- <h3>Alarms</h3> -->
      </AlarmContainer>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import GaugeContainer from './components/GaugeContainer.vue'
import AlarmContainer from './components/AlarmContainer.vue'
import ControlPanel from './components/ControlPanel.vue'
import LineChart from './components/LineChart.vue';

export default defineComponent({
  name: 'App',
  components: {
    GaugeContainer,
    AlarmContainer,
    ControlPanel,
    LineChart
},
});
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: #1b213b;
  font-family: sans-serif;
}

h3 {
  width: 100%;
  display: block;
  margin: 0;
  padding: 0;
  font-weight: 600;
  font-size: 2rem;
  color: #F2F2F2;
  text-align: center;
}

#app-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  padding: 30px;
}

#left-side {
  width: 75%;
}

#right-side {
  width: 25%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

@media only screen and (max-width: 1280px) {
  #app-container {
    display: block;
  }
  #left-side {
    transition: width;
    transition-duration: 0.5s;
    transition-timing-function: ease-in-out;
    width: 100%;
  }
  #right-side {
    transition: width;
    transition-duration: 0.5s;
    transition-timing-function: ease-in-out;
    width: 100%;
  }
}
</style>
