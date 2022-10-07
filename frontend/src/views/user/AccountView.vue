<template>
    <v-card>
        <v-card-title class="text-center justify-center py-6">
            My Account
        </v-card-title>
        <v-spacer />
        <v-row class="justify-center" dense>
            <v-avatar size="150px">
                <img src="https://gogeticon.net/files/1925428/fa0cbc2764f70113bf2fad3905933545.png" />
            </v-avatar>
        </v-row>
        <v-row class="justify-center pb-5">
            <span class="title text-secondary py-2 font-weight-bold">{{ this.user.name }}</span>
        </v-row>
        <v-text-field
            class="ma-2"
            label="Username"
            outlined
            shaped
            prepend-inner-icon="mdi-account"
            :value="this.user.username"
            readonly
            ></v-text-field>
        <v-text-field
            class="ma-2"
            label="E-mail"
            outlined
            shaped
            prepend-inner-icon="mdi-email"
            :value="this.user.email"
            readonly
        ></v-text-field>
        <v-text-field
            class="ma-2"
            label="Last login"
            outlined
            shaped
            prepend-inner-icon="mdi-clock-outline"
            :value="this.user.last_login"
            readonly
        ></v-text-field>
        <v-text-field
            class="ma-2"
            label="Date joined"
            outlined
            shaped
            prepend-inner-icon="mdi-calendar"
            :value="this.user.date_joined"
            readonly
        ></v-text-field>   
    </v-card>
</template>

<script lang="ts">
import AuthUser from '@/models/AuthUser';
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class AccountView extends Vue {

    user: AuthUser | null = this.$store.getters.getUser;
    items = [
        { text: 'Username:', value: 'username' },
        { text: 'Name:', value: 'name' },
        { text: 'E-mail:', value: 'email' },
        { text: 'Last login:', value: 'last_login' },
        { text: 'Date joined:', value: 'date_joined'}
    ];

    async created() {
        try {
            if (!this.user?.username) {
                await this.$router.push({ name: 'dashboard' });
            }
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }
    
}
</script>

<style lang="scss" scoped>
.v-card {
    margin: 80px;
}
</style>