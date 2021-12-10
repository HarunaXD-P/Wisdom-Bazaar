<template>
    <div v-if="value">
        <button @click="closeShow"></button>
    </div>
</template>
<script>
 
    export default {
        data(){
            return{
            }
        },
        props: ["value"],
        model: {
            prop: 'value',
            event: 'balabala'
        },
        methods: {
            changeShow() {
                this.$emit("balabala",false);
            }
        },
    }
</script>
<style >
</style>
