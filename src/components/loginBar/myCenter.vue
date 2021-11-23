<!-- 将原来右侧的个人信息已到右上角的边栏，伴随调整myHeader的高度 -->
<template>
  <div>
    <span class="mycenter">
      <img src="logo.jpg" id="myphoto" /><img />
      <span id="navi-menu">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <el-menu-item index="1">我的消息</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的商品</template>
            <el-menu-item index="2-1" @click="gotoMyGoods">我发布的</el-menu-item>
            <el-menu-item index="2-2">我拍下的</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">这个菜单干什么好呢</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3">个人设置</el-menu-item>
          <el-menu-item index="4" style="margin=0px;"
            ><a href="https://www.ele.me" target="_blank"
              >订单管理</a
            ></el-menu-item
          >
        </el-menu>
      </span>
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },

  components: {},

  computed: {},

  mounted: {},

  methods: {
    gotoMyGoods(){
      this.$router.replace('/myGoods');
    }
  },
};
</script>

<style>
.mycenter {
  float: right;
  margin:auto;
  height:70px;
}
#myphoto {
  margin: auto;
  width: 70px;
  height: 70px;
  float: left;
}
#navi-menu {
  width: 500px;
  float: left;
}
</style>