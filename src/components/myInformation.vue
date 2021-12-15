<!-- right side,for my information and menu -->
<template>
  <div class="information" id="bgr">
    <div>
      <img
        src="../assets/logo.jpg"
        width="200"
        height="150"
        id="image"
        @click="gotoGerenzhuye"
        border-radius="10xp"
      /><img />
      <el-col :span="24" id="item">
        <span style="font-size:36px">{{userName}}</span>
        <el-menu
          default-active="0"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#696969"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="1" class="Item">
            <i class="el-icon-message"></i>
            <span style="font-size:18px">我的消息</span>
          </el-menu-item>

          <el-menu-item index="2" class="Item">
            <i class="el-icon-shopping-cart-2"></i>
            <span slot="title" style="font-size:18px"> 购物车</span>
          </el-menu-item>

          <el-menu-item index="3" class="Item">
            <i class="el-icon-star-on"></i>
            <span slot="title" style="font-size:18px">收藏夹</span>
          </el-menu-item>

          <el-menu-item index="4" class="Item">
            <i class="el-icon-setting"></i>
            <span slot="title" style="font-size:18px" @click="gotoCreate">设置</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
  </div>
</template>

<script>
import GLOBAL from '@/global/global'
export default {
  data(){
    return{
      userName:GLOBAL.currentUser_name,
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    gotoCreate(){
      this.$router.replace('/createItem')
    },
    gotoGerenzhuye()
    {
      this.$router.replace('/gerenzhuye')
    }
  },
};
</script>

<style>
#bgr {
  width: 260px;
  float: left;
  margin-top: 30px;
  /*margin-right: 2%;*/
  position: relative;
  /*right:-200px;*/
  margin-right : 20px;
  border-radius: 25px;
  background: #696969;
  display: flex;
  height: 600px;
}
#id {
  widows: 317px;
}
#image {
  margin: 30px;
}
.Item{
  margin:10px;
}
</style>