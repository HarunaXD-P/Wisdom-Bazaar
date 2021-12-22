<!--根据https://element.eleme.cn/#/zh-CN/component/menu改编-->
<template>
  <div class="Display">
    <el-container class="panal1">
      <el-header height="160px">
        <!--<img src="../assets/iphone.jpeg" width="240px" height="160px" />-->
        <img :src=goodsDisplay.photo class="pic">
      </el-header>
      <!--<img src="../assets/logo.png">-->

      <el-main style = "padding: 10px;">
        <body class="product">
          {{ goodsDisplay.product_name }}
        </body>

        <body class="introduction">
          {{ goodsDisplay.description }}
        </body>
        
      </el-main>
      <el-footer>
        <!--这里要再加一个el-container，不然9999和联系这两个会纵向排列-->
        <!--el-container子元素中有 el-header 或 el-footer 时为 vertical，否则为 horizontal-->
		<body class="price">
		  ￥{{ goodsDisplay.price }}
		</body>
        <el-button class="button" @click="gotoDetail"> 查看 </el-button>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import GLOBAL from "@/global/global";
import axios from "axios";
export default {
  name: "Display",
  props:['goodsContent'],
  data() {
    return {
      title: GLOBAL.title,
      description: GLOBAL.description,
      price: GLOBAL.price,
      picture: GLOBAL.picture,
      goodsDisplay:this.goodsContent,
	    product_id:this.goodsContent.product_id,
    };
  },
  created:function(){
    this.title="myTry";
  },
  methods:{
    gotoDetail(){
      console.log(this.goodsDisplay); 
      this.$router.push({path:'/goodDetail',query:{product_id:this.product_id,}});
    },
  },
};
</script>

<style>
/*一个面板的设置，一共有6个面板*/
.panal1 {
  height: 400px; /*面板高度*/
  background-color: white; /*面板颜色*/
  width: 300px; /*面板宽度 */
  position: relative;
  /*margin: 10px, 10px, 10px, 10px;*/
  border-top: 25px solid white;
  border-radius: 25px;
  box-shadow:2px 2px 15px rgb(184, 180, 180);
}
/*写着“联系”两个字的按钮*/
.button {
  height: 40px; /*按钮高度*/
  width: 100px; /*按钮宽度*/
  background-color: red; /*按钮的背景颜色*/
  color: white; /*按钮的文字颜色*/
}
.price {
  color: red; /*字体颜色*/
  position: relative;
  margin-top: -35px;
  font-size: 24px;
}
.product {
  color: black;
  font-size: 30px; /*字体大小*/
  
  position: relative;
  margin-left: 5px;
  
  overflow: hidden;
  word-wrap: break-word;
  word-break: break-all;
  text-overflow: ellipsis;
  -webkit-line-clamp: 1;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}
.introduction {
  color: black;
  font-size: 18px;
  color:#708090;
  margin-top:auto;
  position: relative;
  overflow: hidden;
  word-wrap: break-word;
  word-break: break-all;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}
.pic {
	width: 240px;
	height: 160px;
}
</style>