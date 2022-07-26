<template>
    <ControlButton />
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
</style>