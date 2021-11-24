<!--展示我所发布的商品-->
<template>
  <div id="app" style="background-color: #ffffff;">
    <!--整个显示出来的是一个面板，看效果还很不好，之后要改-->
    <router-view/>
    <el-container class="panal">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header>
        <myHeader> </myHeader>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main>
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container>
          <myLeftSidebar></myLeftSidebar>
          <div id='main'>
            占个位置
            <myGoods :myGoodsData="goodsData"></myGoods>
          </div>
        
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
import "element-ui/lib/theme-chalk/index.css";
import goods from "@/components/myGoods"
import GLOBAL from '@/global/global'
import axios from 'axios';
//import MyGoods from '../components/myGoods.vue';
export default {
  name: "App",
  components: {
    myHeader: Header,
    myLeftSidebar: LeftSidebar,
    myDisplay: DisplaySix,
    myInformation: information,
    myGoods:goods,
  },
  data(){
    return{
      goodsData:[{'name':"pppp",'descript':"haisidai"},{'name':"FC31",'descript':"wudaiji"},{'name':"F22","descript":'niangniang'}],
    }
  },

  created(){
      const  path="http://127.0.0.1:5000/userallproducts";
      var searchinfo={
        "user_name":GLOBAL.currentUser_name,
        "user_id":GLOBAL.currentUser_ID,
      }
      axios.post(path,JSON.stringify(searchinfo))
          .then(function(response){
            var myAllProducts=response.data;
            console.log(myAllProducts);
            this.goodsData=myAllProducts;
            GLOBAL.myAllProducts=myAllProducts;


          });
    

    }
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
  width:1920px;
  height:1080px;
  float:center;
  margin:auto;
}
#main{
  width:1500px;
  margin-right: 40pxs;
  height: 1080px;
  background-color: bisque;
}
</style>
