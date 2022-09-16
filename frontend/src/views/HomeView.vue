<template>
  <div class="container">
    <login-card @onSubmit="login"></login-card>
  </div>
</template>

<script lang="ts">
/* eslint-disable */

import { Options, Vue } from 'vue-class-component';
import LoginCard from '../components/LoginCard.vue';
import axios from 'axios';

@Options({
  options: { LoginCard }
})

export default class HomeView extends Vue {

  errors = [];

  async created() {}

  async login(username: string, password: string) {

    console.log(username + ' ' + password);

    axios.defaults.headers.common["Authorization"] = "";

    localStorage.removeItem("token");

    const formData = {
      username,
      password
    }

    axios
      .post("/api/v1/token/login", formData)
      .then(response => {

        const token = response.data.auth_token;

        this.$store.commit('setToken', token)

        axios.defaults.headers.common["Authorization"] = "Token" + token

        localStorage.setItem("token", token)

        this.$router.push('/dashboard')
      })
  }
}

</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  align-content: center;
  height: 100%;

  .v-btn {
    margin: 5px;
    text-decoration: white;
  }
}
</style>
