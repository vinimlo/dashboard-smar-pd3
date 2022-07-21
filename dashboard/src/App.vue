<template>
  <div class="gauge-container">
    <VariableGauge :variableToRead="'level'" />
    <VariableGauge :variableToRead="'temperature'" />
    <VariableGauge :variableToRead="'flow'" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import VariableGauge from './components/VariableGauge.vue'


export default defineComponent({
  name: 'App',
  components: {
    VariableGauge
  },
});
</script>

<style>
.gauge-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
}
</style>
