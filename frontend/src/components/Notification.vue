<template>
    <v-alert
        v-model="dialog"
        type="error"
        close-text="Close Notification"
        dismissable
    >
        {{ messageList.join(', ') }}
    </v-alert>
</template>

<script lang="ts">
import { Vue, Options } from 'vue-class-component';

export default class Notification extends Vue {

}


</script>