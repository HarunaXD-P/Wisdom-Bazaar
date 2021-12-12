<!--根据https://element.eleme.cn/#/zh-CN/component/menu改编-->
<template>
  <div class="LeftSidebar">
    <el-row class="tac">
      <el-col :span="24">
        <span style="font-size: 24px;font-weight: 500;">商品分类</span>
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#696969"
          text-color="#fff"
          active-text-color="#ffd04b"
		  >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-cpu"></i>
              <span>数码产品</span>
            </template>
            <el-menu-item-group>
              <template slot="title">手机</template>
              <el-menu-item index="1-1" @click="getclick11()">苹果手机</el-menu-item>
              <el-menu-item index="1-2" @click="getclick12()">安卓手机</el-menu-item>
            </el-menu-item-group>
            <el-menu-item index="1-3" @click="getclick13()">数码配件</el-menu-item>
            <el-menu-item index="1-4" @click="getclick14()">影音设备</el-menu-item>
          </el-submenu>
          <el-menu-item index="2" @click="getclick2()">
            <i class="el-icon-shopping-bag-1"></i>
            <span slot="title">二手衣物</span>
          </el-menu-item>
          <el-menu-item index="3" @click="getclick3()">
            <i class="el-icon-document"></i>
            <span slot="title">票务转让</span>
          </el-menu-item>
          <el-menu-item index="4" @click="getclick4()">
            <i class="el-icon-water-cup"></i>
            <span slot="title">生活用品</span>
          </el-menu-item>
          <el-menu-item index="5" @click="getclick5()"> 
            <i class="el-icon-basketball"></i>
            <span slot="title">运动装备</span>
          </el-menu-item>
          <el-menu-item index="6" @click="getclick6()">
            <i class="el-icon-reading"></i>
            <span slot="title">二手书本</span>
          </el-menu-item>
          <el-menu-item index="7" @click="getclick7()"> 
            <i class="el-icon-discount"></i>
            <span slot="title">其他二手</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data(){
    return{
      index_selected:'default-active',
    }


  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    getclick11(){
      this.index_selected=11;
      console.log(this.index_selected);
    },
    getclick12(){
      this.index_selected=12;
      console.log(this.index_selected);
    },
    getclick13(){
      this.index_selected=13;
      console.log(this.index_selected);
    },
    getclick14(){
      this.index_selected=14;
      console.log(this.index_selected);
    },
    getclick2(){
      this.index_selected=2;
      console.log(this.index_selected);
    },
    getclick3(){
      this.index_selected=3;
      console.log(this.index_selected);
    },
    getclick4(){
      this.index_selected=4;
      console.log(this.index_selected);
    },
    getclick5(){
      this.index_selected=5;
      console.log(this.index_selected);
    },
    getclick6(){
      this.index_selected=6;
      console.log(this.index_selected);
    },
    getclick7(){
      this.index_selected=7;
      console.log(this.index_selected);
    },

  },
};
</script>

<style>
.tac {
  
  position: relative; /*位置为相对位置*/
  margin-left: 20px; /*排布在左侧*/
  top:-0px;
  width:200px; /*宽度*/
  
  /*以下两条共同设置边框颜色，如果不设置border-style会显示不出效果*/
}
.el-ment-item {
  width:300px;
}

</style>