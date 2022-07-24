<template>
  <div class="gauge-container">
    <slot></slot>
    <GaugeIndicator v-for="(variableToRead, index) in variableItems" :key="index" :variableToRead="variableToRead" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import GaugeIndicator from './GaugeIndicator.vue';

export default defineComponent({
  name: 'GaugeContainer',
  components: {
    GaugeIndicator
  },
  props: {
    variableItems: {
      type: Array as PropType<Array<string>>,
      default: () => []
    }
  }
});
</script>

<style scoped>
.gauge-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  padding: 15px 0;
}
</style>