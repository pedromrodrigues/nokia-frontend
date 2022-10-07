import Switch from '@/models/Switch';
import RemoteServices from '@/services/RemoteServices';
import Vue from 'vue'
import Vuex from 'vuex'
import AuthUser from '@/models/AuthUser'
import Container from '@/models/Container'

interface State {
  token: string;
  user: AuthUser | null;
  isAuthenticated: boolean;
  currentContainer: Container | null;
  currentSwitch: Switch | null;
  error: boolean;
  errorMessage: string;
  notification: boolean;
  notificationMessageList: string[];
  loading: boolean;
}

const state: State = {
  token: '',
  user: null,
  isAuthenticated: false,
  currentContainer: null,
  currentSwitch: null,
  error: false,
  errorMessage: '',
  notification: false,
  notificationMessageList: [],
  loading: false,
};

Vue.use(Vuex);
Vue.config.devtools = true;

export default new Vuex.Store({
  state: state,
  mutations: {
    initializeStore(state) {
      const token = localStorage.getItem('token');
      if (token) {
        state.token = token;
        state.isAuthenticated = true
      } else {
        state.token = '',
        state.isAuthenticated = false
      }
      const user = localStorage.getItem('user');
      if (user) {
        state.user = JSON.parse(user);
      }
    },
    login(state, token: string) {
      localStorage.setItem('token', token);
      state.token = token;
      state.isAuthenticated = true;
    },
    logout(state) {
      localStorage.setItem('token', '');
      state.token = '';
      localStorage.setItem('user', '');
      state.user = null;
      localStorage.setItem('currentContainer', '');
      state.currentContainer = null;
      state.isAuthenticated = false;
    },
    setUser(state, user: AuthUser) {
      localStorage.setItem('user', JSON.stringify(user));
      state.user = user;
    },
    currentContainer(state, currentContainer: Container) {
      localStorage.setItem('currentContainer', JSON.stringify(currentContainer));
      state.currentContainer = currentContainer;
    },
    currentSwitch(state, currentSwitch: Switch) {
      localStorage.setItem('currentSwitch', JSON.stringify(currentSwitch));
      state.currentSwitch = currentSwitch;
    },
    error(state, errorMessage: string) {
      state.error = true;
      state.errorMessage = errorMessage;
    },
    clearError(state) {
      state.error = false;
      state.errorMessage = '';
    },
    notification(state, notificationMessageList: string[]) {
      state.notification = true;
      state.notificationMessageList = notificationMessageList;
    },
    clearNotification(state) {
      state.notification = false;
      state.notificationMessageList = [];
    },
  },
  actions: {
    async login({ commit }, formData) {
      const token = await RemoteServices.login(formData.username, formData.password);
      commit('login', token);
      const user = await RemoteServices.getUser();
      commit('setUser', user);
    },
    logout({ commit }) {
      return new Promise<void>((resolve) => {
        commit('logout');
        resolve();
      });
    },
    error({ commit }, errorMessage) {
      commit('error', errorMessage);
    },
    clearError({ commit }) {
      commit('clearError');
    },
    notification({ commit }, notification) {
      commit('notification', notification);
    },
    clearNotification({ commit }) {
      commit('clearNotification');
    },
    currentContainer({ commit }, currentContainer) {
      commit('currentContainer', currentContainer);
    },
    currentSwitch({ commit }, currentSwitch) {
      commit('currentSwitch', currentSwitch);
    }
  },
  modules: {
  },
  getters: {
    getToken(state): string {
      return state.token;
    },
    getUser(state): AuthUser | null {
      return state.user;
    },
    getError(state): boolean {
      return state.error;
    },
    getErrorMessage(state): string {
      return state.errorMessage;
    },
    getNotification(state): boolean {
      return state.notification;
    },
    getNotificationMessageList(state): string[] {
      return state.notificationMessageList;
    },
    getCurrentContainer(state): Container | null {
      return state.currentContainer;
    },
    getCurrentSwitch(state): Switch | null {
      return state.currentSwitch;
    }
  },
})
