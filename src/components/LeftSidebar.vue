<!--根据https://element.eleme.cn/#/zh-CN/component/menu改编-->
<template>
  <div class="LeftSidebar">
    <el-row class="tac">
      <el-col :span="24">
        <!--标题-->
        <h5 style="font-size:60px">分类</h5>
        <!--设置一些属性，比如文字颜色等-->
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          text-color="#20B2AA"
          @open="handleOpen"
          @close="handleClose"
        >
          <!--下面的一堆子目录-->
          <!--font-size设置字体大小-->
          <el-menu-item-group >
              <el-menu-item index="1-1" style="font-size:40px" class="Items">二手书本</el-menu-item>
              <el-menu-item index="1-2" style="font-size:40px" class="Items">数码产品</el-menu-item>
              <el-menu-item index="1-3" style="font-size:40px" class="Items">票务转让</el-menu-item>
              <el-menu-item index="1-4" style="font-size:40px" class="Items">二手衣物</el-menu-item>
              <el-menu-item index="1-5" style="font-size:40px" class="Items">生活用品</el-menu-item>
              <el-menu-item index="1-6" style="font-size:40px" class="Items">运动装备</el-menu-item>
              <el-menu-item index="1-7" style="font-size:40px" class="Items">其他二手</el-menu-item>
          </el-menu-item-group>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
.tac {
  background-color: #e1ffff; /*“分类”这个小框的背景颜色*/
  position: relative; /*位置为相对位置*/
  left: 0; /*排布在左侧*/
  width: 300px; /*宽度*/
  
  top: 200px;
  /*以下两条共同设置边框颜色，如果不设置border-style会显示不出效果*/
  border-style: solid;
  border-color: #696969;
  /*设置上面两个为圆角 */
  border-radius: 25px;
  margin-top: -120px;
  margin-left: 20%;
}
.el-menu-vertical-demo {
  background-color: #e1ffff; /*设置下面七个子目录的背景颜色 */
  /*在下面七个子目录的上面添一条线，因为ppt的图里“分类”和“二手书本”之间是有一条线隔开的*/
  border-top: 2px solid #696969;
  /*设置右下为圆角 */
  border-end-end-radius: 25px;
  /*设置左下为圆角 */
  border-end-start-radius: 25px;
}
.LeftSidebar {
  /*设置“分类”这两个字的字体颜色*/
  color: #20b2aa;
}
/*设置Items之间的间距 */
.Items{
  margin:50px 10px;
}
</style>