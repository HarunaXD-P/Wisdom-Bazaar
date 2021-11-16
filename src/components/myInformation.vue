<!-- right side,for my information and menu -->
<template>
  <div class="information" id="bgr">
    <div>
      <img
        src="../assets/logo.jpg"
        width="200"
        height="150"
        id="image"
      /><img />
      <el-col :span="24" id="item">
        <h3 style="font-size:60px">用户名</h3>
        <el-menu
          default-active="0"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="1" class="Item">
            <i class="el-icon-message"></i>
            <span style="font-size:40px">我的消息</span>
          </el-menu-item>

          <el-menu-item index="2" class="Item">
            <i class="el-icon-shopping-cart-2"></i>
            <span slot="title" style="font-size:40px"> 购物车</span>
          </el-menu-item>

          <el-menu-item index="3" class="Item">
            <i class="el-icon-star-on"></i>
            <span slot="title" style="font-size:40px">收藏夹</span>
          </el-menu-item>

          <el-menu-item index="4" class="Item">
            <i class="el-icon-setting"></i>
            <span slot="title" style="font-size:40px" @click="gotoCreate">设置</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
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
    gotoCreate(){
      this.$router.replace('/createItem')
    }
  },
};
</script>

<style>
#bgr {
  width: 317px;
  float: right;
  height: 1100px;
  margin-top: 75px;
  /*margin-right: 2%;*/
  position: relative;
  right:-200px;
  margin-left : 80px;
  border-radius: 25px;
  background: #545c64;
}
#id {
  widows: 317px;
}
#image {
  margin: 30px;
}
.Item{
  margin:93px 10px;
}
</style>