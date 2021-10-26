<!--这个文件可以理解成一个整体显示的效果，主要是将其余个组件放在一个网页中-->
<template>
  <div id="app">
    <!--整个显示出来的是一个面板，看效果还很不好，之后要改-->

    <el-container class="panal">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header>
        <Header> </Header>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main class="mainContent">
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container>
          <myLeftSidebar></myLeftSidebar>
          <!--<router-view/>-->
          <myDisplay></myDisplay>
          <myInfirmation></myInfirmation>
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import myHeader from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
import "element-ui/lib/theme-chalk/index.css";
export default {
  name: "App",
  components: {
    Header: myHeader,
    myLeftSidebar: LeftSidebar,
    myDisplay: DisplaySix,
    myInfirmation: information,
  },
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
