import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/page/login'
import Home from '@/page/homePage'
import Register from '@/page/register'
import Findpassword from '@/page/findpassword'
import CreateItem from '@/page/createItem'
import gerenzhuye from '@/page/gerenzhuye'
import detail from '@/page/goodDetail'
import showMyGoods from '@/page/showMyGoods'
import seekforGoods from '@/page/seekGoods'
import publish from '@/page/publishPage'
import Search from '@/page/search'
import contact from '@/page/contact'
import Searchbytag from '@/page/searchbytag'
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
	{
		path: '/register',
		name: 'Register',
		component: Register,
	},
	{
		path: '/findpassword',
		name: 'Findpassword',
		component: Findpassword,
	},
  {
    path: '/createItem',
    name: 'CreateItem',
    component: CreateItem,
  },
  {
    path: '/gerenzhuye',
    name: 'Gerenzhuye',
    component: gerenzhuye,
  },
  {
    path: '/goodDetail',
    name: 'GoodDetail',
    component: detail,
  },
  {
    path:'/myGoods',
    name:'showMyGoods',
    component:showMyGoods,
  },
  {
    path:'/seekGoods',
    name:seekforGoods,
    component:seekforGoods,
  },
  {
    path:'/putGoods',
    name:publish,
    component:publish,
  },
  {
    path:'/search',
    name:'Search',
    component:Search,
  },
  {
    path:'/contact',
    name:contact,
    component:contact,
  },
  {
	path:'/tag',
	name:'Searchbytag',
	component:Searchbytag,
  },
  ]
})
