import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import VueApexCharts from 'vue3-apexcharts'

const app = createApp(App);
app.use(VueApexCharts).mount('#app');

// createApp(App).mount('#app')
