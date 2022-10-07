
<template>
    <nav>
        <v-app-bar clipped-left color="#27439c" dense dark elevation="4">
            <v-app-bar-nav-icon 
                v-if="$store.state.isAuthenticated"
                @click.stop="drawer = !drawer"
            ></v-app-bar-nav-icon>
            <v-app-bar-title
                v-if="$store.state.isAuthenticated"
            >Menu
            </v-app-bar-title>
            <v-spacer />

            <v-btn
                v-if="$store.state.isAuthenticated"
                dark
                text
                color="white"
                @click="logout"
            > 
            Logout
            </v-btn>

        </v-app-bar>
        <v-navigation-drawer
            v-if="$store.state.isAuthenticated"
            v-model="drawer"
            absolute
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
                <v-list-item-group
                    v-model="selectedItem"
                    color="primary"
                >
                    <v-list-item
                        v-for="item in items"
                        :key="item.text"
                        @click="forwarding(item.text)"
                    >
                        <v-list-item-icon>
                            <v-icon v-text="item.icon"></v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title v-text="item.text"></v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script lang="ts">
/* eslint-disable */
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class TopBar extends Vue {
    appName: string = process.env.VUE_APP_NAME || 'ENV FILE MISSING';
    drawer: boolean = false;
    selectedItem = '';

    items = [
        { text: 'Switches', icon: 'mdi-server-network' },
        { text: 'Containers', icon: 'mdi-router-network' },
        { text: 'Account', icon: 'mdi-account' },
    ];

    async logout() {
        await this.$store.dispatch('logout');
        await this.$router.push({ name: 'home' }).catch(() => {});
    }

    async forwarding(option: string) {
        if (option === 'Containers') {
            if ( this.$route.name === 'dashboard' ) {
                this.$router.go(0);
            } else {
                this.$router.push({ name: 'dashboard' }).catch(() => {});
            }
        }
        if (option === 'Account') {
            if (this.$route.name === 'account' ) {
                this.$router.go(0);
            } else {
                this.$router.push({ name: 'account' }).catch(() => {});
            }
        }
        if (option === 'Switches') {
            if (this.$route.name === 'switches') {
                this.$router.go(0);
            } else {
                this.$router.push({ name: 'switches' }).catch(() => {});
            }
        }
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