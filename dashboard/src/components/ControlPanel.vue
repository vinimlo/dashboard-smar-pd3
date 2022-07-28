<template>
    <div class="btn-panel">
        <ControlButton :controlBtnName="'Bomb 1'" :instrument="'bomb_1'" />
        <ControlButton :controlBtnName="'Valve 1'" :instrument="'valve_1'" />
        <ControlButton :controlBtnName="'Heater'" :instrument="'heater'" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ControlButton from './ControlButton.vue'

export default defineComponent({
    name: 'ControlPanel',
    components: {
        ControlButton
    }
});
</script>

<style scoped>
.btn-panel {
    display: flex;
    gap: 25px;
    justify-content: center;
}
</style>