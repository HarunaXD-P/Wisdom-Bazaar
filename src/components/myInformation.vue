<!-- right side,for my information and menu -->
<template>
  <div class="information" id="bgr">
    <div>
      <img
        src="../assets/logo.jpg"
        width="100"
        height="100"
        id="image"
      /><img />
      <el-col :span="24" id="item">
        <h3>用户名</h3>
        <el-menu
          default-active="0"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="1">
            <i class="el-icon-message"></i>
            <span>我的消息</span>
          </el-menu-item>

          <el-menu-item index="2">
            <i class="el-icon-shopping-cart-2"></i>
            <span slot="title"> 购物车</span>
          </el-menu-item>

          <el-menu-item index="3">
            <i class="el-icon-star-on"></i>
            <span slot="title">收藏夹</span>
          </el-menu-item>

          <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">设置</span>
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
  },
};
</script>

<style>
#bgr {
  width: 317px;
  float: right;
  height: 500px;
  margin-top: 75px;
  /*margin-right: 2%;*/
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
</style>