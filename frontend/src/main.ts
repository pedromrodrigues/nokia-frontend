import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import TopBar from './components/TopBar.vue'
import LoginCard from './components/LoginCard.vue'
import axios from 'axios'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App)
  .use(router, axios)
  .use(store)
  .use(vuetify)
  .component('TopBar', TopBar)
  .component('LoginCard', LoginCard)
  .mount('#app')
