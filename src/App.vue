<!--这个文件可以理解成一个整体显示的效果，主要是将其余个组件放在一个网页中-->
<template>
  <div id="app">
    <router-view/>   
  </div>
</template>

<script>
/*
import DevicePixelRatio from './utils/devicePixelRatio';
*/
export default {
	/*data() {
	        return {
	            fullWidth: document.documentElement.clientWidth
	        };
	    },*/
  name: "App",
  /*
  created() {
      new DevicePixelRatio().init();
  	}
	
   computed: {
           ...mapGetters(['stageWidth'])
       },
       methods: {
           handleResize() {
               let that = this;
               that.fullWidth = document.documentElement.clientWidth;
               if (that.fullWidth < 768 && that.stageWidth == 'large') {
                   that.$store.dispatch('app/changeWidth', 'small');
               }
               if (that.fullWidth > 768 && that.stageWidth == 'small') {
                   that.$store.dispatch('app/changeWidth', 'large');
               }
           }
       },
       created() {
           if (this.fullWidth < 768 && this.stageWidth == 'large') {
               this.$store.dispatch('app/changeWidth', 'small');
           }
           if (this.fullWidth > 768 && this.stageWidth == 'small') {
               this.$store.dispatch('app/changeWidth', 'large');
           }
           window.addEventListener('resize', this.handleResize);
       },
       beforeDestroy: function() {
           window.removeEventListener('resize', this.handleResize);
       }*/
};

</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 20px;
  margin-right : 0px;*/
  margin: auto;
  min-height:1080px;
  min-width: 1280px;
}
.mainContent{
  float:center;
  margin:auto;
}
</style>
