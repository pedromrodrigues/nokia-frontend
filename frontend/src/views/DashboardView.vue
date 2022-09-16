<template>
    <v-card>
        <v-card-title>
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
            ></v-text-field>
        </v-card-title>
    </v-card>
            

</template>

<script lang="ts">
import { Vue } from 'vue-class-component';
import axios from 'axios';
import Container from '../models/Container';

export default class DashboardView extends Vue {

    containers: Container[] = [];
    search = '';

    async created() {
        try {
            console.log("OLA")
            //console.log(this.containers.length)
            this.containers = await this.get_containers()
            console.log(this.containers)
            for (let i = 0; i < this.containers.length; i++) {
                console.log(this.containers[i].name)
            }
        } catch (error) {
            console.log("ERROOO " + error)
        }
    }

    async get_containers(): Promise<Container[]> {

        return axios
            .get('api/v1/containers')
            .then(response => {
                //for (let i = 0; i < response.data.length; i++) {
                //    console.log(response.data[i])
                //}

                return response.data.map((container: any) => {
                    return new Container(container);
                })
            })
            .catch(async (error) => {
                console.log(JSON.stringify(error))
            })
    }



}
</script>

<style lang="scss" scoped>

.v-card {
    //display: flex;
    margin-top: 100px;
    margin: 100px;
    //padding-top: 100px;

    
    
}
</style>