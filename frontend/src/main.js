import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import { VLazyImagePlugin } from "v-lazy-image";
 

import VueAwesomeSwiper from 'vue-awesome-swiper'

// import style
import 'swiper/css/swiper.css'


Vue.use(VueAwesomeSwiper, /* { default options with global component } */)
Vue.use(VLazyImagePlugin);


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
