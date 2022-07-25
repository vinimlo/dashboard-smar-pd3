<template>
  <div class="alarm-container">
    <slot></slot>
    <AlarmIndicator v-for="(alarmToRead, index) in alarmItems" :key="index" :alarmToRead="alarmToRead" :alarm-name="alarmToRead.split('_').slice(1,undefined).join(' ').toUpperCase()"/>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import AlarmIndicator from './AlarmIndicator.vue';

export default defineComponent({
  name: 'AlarmContainer',
  components: {
    AlarmIndicator
  },
  props: {
    alarmItems: {
      type: Array as PropType<Array<string>>,
      default: () => []
    }
  },
  data() {
    return {
      isActive: false
    }
  }
});
</script>

<style scoped>
.alarm-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  padding: 15px 0;
}
</style>