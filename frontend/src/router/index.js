import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/current-exhibitions',
    name: 'currentexhibitions',
    component: () => import(/* webpackChunkName: "currentexibitions" */ '../views/CurrentExhibiton.vue')
  },
  {
    path: '/current-exhibitions/:id',
    name: 'ExhibitionDetail',
    component: () => import(/* webpackChunkName: "exhibitionDetail" */ '../views/ExhibitionDetail.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
