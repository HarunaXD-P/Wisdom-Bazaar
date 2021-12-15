<!--根据https://element.eleme.cn/#/zh-CN/component/menu改编-->
<!--
<template>
  <div class="Display">
    <el-container class="panal1">
      <el-header height="90px">
        <img src="../assets/iphone.jpeg" width="240px" height="160px" />
      </el-header>-->
      <!--<img src="../assets/logo.png">-->
      <!--
      <el-main>
        <body class="product">
          iphone13手机
        </body>

        <body class="introduction">
          非常的新鲜，非常的美味，99新男生自用
        </body>
      </el-main>
      <el-footer>-->
        <!--这里要再加一个el-container，不然9999和联系这两个会纵向排列-->
        <!--el-container子元素中有 el-header 或 el-footer 时为 vertical，否则为 horizontal-->
        <!--
        <el-container>
          <body class="price">
            ￥9999
          </body>
          <el-button class="button"> 联系 </el-button>
        </el-container>
      </el-footer>
    </el-container>
  </div>
</template>
-->

<template>
  <div class="DisplayOld">
    <el-container class="panal1">
      <el-header height="90px">
        <img src="../assets/iphone.jpeg" width="240px" height="160px" />
      </el-header>
      <!--<img src="../assets/logo.png">-->

      <el-main>
        <body class="product">
          数学分析
        </body>

        <body class="introduction">
          bookdfa
        </body>
        <body class="price">
          $79.99
        </body>
      </el-main>
      <el-footer>
        <!--这里要再加一个el-container，不然9999和联系这两个会纵向排列-->
        <!--el-container子元素中有 el-header 或 el-footer 时为 vertical，否则为 horizontal-->

        <el-button class="button"> 查看 </el-button>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "DisplayOld",
  data() {
    active(0)
  },
};
</script>

<style>
/*一个面板的设置，一共有6个面板*/
.panal1 {
  height: 400px; /*面板高度*/
  background-color: #f0fff0; /*面板颜色*/
  width: 300px; /*面板宽度 */
  position: relative;

  /*margin: 10px, 10px, 10px, 10px;*/
  border-top: 25px solid #f0fff0;
  border-radius: 25px;
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
  top: 50px;
}
.product {
  color: black;
  font-size: 30px; /*字体大小*/
  text-align: left;
  position: relative;
  top: 50px;
}
.introduction {
  color: black;
  font-size: 20px;
  text-align: left;
  position: relative;
  width: 244px;
  word-wrap: break-word;
  word-break: break-all;
  text-overflow: ellipsis;
  -webkit-line-clamp: 3;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  top: 50px;
  overflow: hidden;
}
</style>