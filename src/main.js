import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import VueRouter from 'vue-router'

Vue.use(ElementUI);

Vue.config.productionTip = false

const routes = [
	{ path:'../register', component: registerlink },
	//{ path:'../findpassword', component: findpassword }
]

const router = new VueRouter({
	routes
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
