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
import { Vue, Component, Watch } from 'vue-property-decorator';

@Component
export default class Notification extends Vue {
    dialog: boolean = this.$store.getters.getNotification;
    messageList: string = this.$store.getters.getNotificationMessageList;

    created() {
        this.dialog = this.$store.getters.getNotification;
        this.messageList = this.$store.getters.getNotificationMessageList;
        this.$store.watch(
            (state, getters) => getters.getNotification,
            () => {
                this.dialog = this.$store.getters.getNotification;
                this.messageList = this.$store.getters.getNotificationMessageList;
            }
        );
    }

    @Watch('dialog')
    closeNotification() {
        if (!this.dialog) {
            this.$store.dispatch('clearNotification');
        }
    }
}

</script>

<style lang="scss" scoped>
.v-alert {
    z-index: 9999;
    position: absolute;
    left: 20px;
    top: 80px;
    width: calc(100% - 40px);
}
</style>