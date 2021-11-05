<!--这个文件可以理解成一个整体显示的效果，主要是将其余个组件放在一个网页中-->
<template>
  <div id="app">
    <router-view/>   
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-right : 0px;
}
.mainContent{
  float:center;
  margin:auto;
}
</style>
