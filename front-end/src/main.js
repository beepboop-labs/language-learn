import { createApp } from 'vue'
import App from './App.vue'
import router from "./router";
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faBars, faUserSecret } from '@fortawesome/free-solid-svg-icons'

library.add(faBars)
const app = createApp(App);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount("#app");

// import './assets/main.css'

// createApp(App).mount('#app')
