import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DashboardView from '@/views/DashboardView.vue'
import SwitchApplicationsView from '@/views/switch/SwitchApplicationsView.vue'
import InterfacesView from '@/views/applications/InterfacesView.vue';
import VrfsView from '@/views/applications/VrfsView.vue';
import LldpView from '@/views/applications/LldpView.vue';
import AccountView from '@/views/user/AccountView.vue';
import SwitchesView from '@/views/switch/SwitchesView.vue';

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  },
  {
    path: '/switches',
    name: 'switches',
    component: SwitchesView
  },
  {
    path: '/switches/:hostname',
    name: 'switch-options',
    component: SwitchApplicationsView,
  },
  {
    path: '/switches/:hostname/interfaces',
    name: 'interfaces',
    component: InterfacesView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: { title: 'SR LINUX', requiredAuth: 'None' },
  },
  {
    path: '/switches/:hostname/vrfs',
    name: 'vrfs',
    component: VrfsView,
    props: (route) => ({ vrf_type: route.query.vrf_type }),
  },
  {
    path: '/switches/:hostname/lldp',
    name: 'lldp',
    component: LldpView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
