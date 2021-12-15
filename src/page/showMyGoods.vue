<!--展示我所发布的商品-->
<template>
  <div id="showmygoods" style="background-color: #ffffff;">
    <!--整个显示出来的是一个面板，看效果还很不好，之后要改-->
    <router-view/>
    <el-container class="panal">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header style="padding: unset;">
        <myHeader> </myHeader>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main style="padding: unset;">
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container>
          <myLeftSidebar></myLeftSidebar>
          <div id='main'>
            <div>你发布的商品共{{goodsData.length}}件</div>
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
      goodsData:GLOBAL.myAllProducts,
      /*
      goodsData:[{"product_id": 3, "product_name": "\u8f6f\u5de5", "category_value": 1, "price": 70.1, "photo": null, "description": "\u8f6f\u4ef6\u5de5\u7a0b\u6559\u6750", "source_id": 1}, 
                {"product_id": 4, "product_name": "yxd", "category_value": 2, "price": 100000.0, "photo": null, "description": "\u4fe1\u79d1\u5927\u4e09\u672c\u79d1\u751f", "source_id": 1}]
      */
    }
  },

  created(){
      /*
      const  path="http://127.0.0.1:5000/userallproducts";
      var searchinfo={
        "user_name":GLOBAL.currentUser_name,
        "user_id":GLOBAL.currentUser_ID,
      }
      axios.post(path,JSON.stringify(searchinfo))
          .then(function(response){
            var myAllProducts=response.data;
            //console.log(myAllProducts);
            //console.log("this is all my products")
            this.goodsData=myAllProducts;
            GLOBAL.myAllProducts=myAllProducts;
            //console.log("howmany?")
            //console.log(myAllProducts.length)


          });
      console.log("initial the page");
      console.log(this.goodsData);
      console.log(this.goodsData.length);
      */
    

    }
};
</script>

<style>
#showmygoods {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-right : 0px;
  min-height:1080px;
  float:center;
  margin:auto;
}
#main{
  width:1500px;
  margin-right: 40pxs;
  margin-top: 30px;
  min-height: 1080px;
  background-color: bisque;
}
</style>
