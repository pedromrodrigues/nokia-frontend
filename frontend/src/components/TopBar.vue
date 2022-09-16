
<template>
    <nav>
        <v-app-bar clipped-left color="#27439c" dense dark elevation="4">
            <v-app-bar-nav-icon 
                v-if="$store.state.isAuthenticated"
                @click.stop="drawer = !drawer"
                color="white"
            ></v-app-bar-nav-icon>
            <v-spacer />

            <v-btn
                v-if="$store.state.isAuthenticated"
                dark
                text
                color="white"
            > 
            Logout
            </v-btn>

        </v-app-bar>
        <v-navigation-drawer
            v-if="$store.state.isAuthenticated"
            v-model="drawer"
            absolute
            bottom
            temporary
        >
            <v-list
                nav
                dense
            >
                <v-list-item>
                    <v-list-item-title>
                    Monitor App
                    </v-list-item-title>
                    <v-list-item-subtitle>Nokia SR Linux</v-list-item-subtitle>
                </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-list>
                <v-list-item>
                    <v-list-item-title>Containers</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script lang="ts">
/* eslint-disable */
import { Options, Vue } from 'vue-class-component';
import axios from 'axios';

export default class TopBar extends Vue {
    appName: string = process.env.VUE_APP_NAME || 'ENV FILE MISSING';
    drawer: boolean = false;

    async logout() {

        console.log("Logging out...")

        axios
            .post("/api/v1/token/logout/")
            .then(response => {
                axios.defaults.headers.common["Authorization"] = ""

                localStorage.removeItem("token")

                this.$store.commit('removeToken')

                this.$router.push('/')
            })
    }
}
</script>


<style lang="scss" scoped>
.no-active::before {
    opacity: 0 !important;
}

nav {
    z-index: 300;
}
</style>