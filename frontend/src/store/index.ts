import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      username: '',
      isAdmin: false
    },
    isAuthenticated: false,
    token: ''
  },
  getters: {
    
  },
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
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = '',
      state.isAuthenticated = false
    },
    setAdmin(state) {
      state.user.isAdmin = true
    }
  },
  actions: {
  },
  modules: {
  }
})
