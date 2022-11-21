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
import NotFoundView from '@/views/NotFoundView.vue';
import SoftwareAgentState from '@/components/agent/SoftwareAgentState.vue';
import SwitchConfigurations from '@/components/applications/SwitchConfigurations.vue';
import Store from '@/store';

Vue.use(VueRouter)

const APP_NAME = process.env.VUE_APP_NAME || '';

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { title: APP_NAME, requiredAuth: 'None' },
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView,
    meta: { title: APP_NAME + ' - Account', requiredAuth: true },
  },
  {
    path: '/switches',
    name: 'switches',
    component: SwitchesView,
    meta: { title: APP_NAME + ' - Switches', requiredAuth: true },
  },
  {
    path: '/switches/:hostname',
    name: 'switch-options',
    component: SwitchApplicationsView,
    meta: { title: APP_NAME + ' - Switch Applications', requiredAuth: true },
  },
  {
    path: '/switches/:hostname/interfaces',
    name: 'interfaces',
    component: InterfacesView,
    meta: { title: APP_NAME + ' - Switch Interfaces', requiredAuth: true },
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
    meta: { title: APP_NAME + ' - Switch VRF', requiredAuth: true },
  },
  {
    path: '/switches/:hostname/lldp',
    name: 'lldp',
    component: LldpView,
    meta: { title: APP_NAME + ' - Switch LLDP', requiredAuth: true },
  },
  {
    path: '**',
    name: 'not-found',
    component: NotFoundView,
    meta: { title: 'Page Not Found', requiredAuth: 'None' },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

router.beforeEach(async (to, from, next) => {
  if (to.meta?.requiredAuth == 'None') {
    next();
  }
  if (to.meta?.requiredAuth == true && Store.getters.isAuthenticated) {
    next();
  } else {
    next('/');
  }
});

router.afterEach(async (to, from) => {
  document.title = to.meta?.title;
});

export default router
