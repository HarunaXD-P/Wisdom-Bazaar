import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/page/login'
import Home from '@/page/homePage'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component : Home,
    },
    {
      path:'/login',
      name:'Login',
      component: Login,
    },
  ]
})
