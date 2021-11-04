<template>
  <div style="background-color: #ebebeb; min-height: 2000px; width:1920px; margin:auto">
    <div
      style="
        height: 70px;
        width: 1920px;
        background-color: #3896c2;
        overflow: hidden;
      "
    >
      <span class="header" id="logo"> FairMart </span>
      <span class="header" id="search">
        <el-input
          placeholder="请输入"
          icon="search"
          v-model="searchCriteria"
          :on-icon-click="handleIconClick"
        >
        </el-input>
      </span>
      <span class="header" id="login">
        <!--这里加了一个跳转到登陆的功能-->
        <el-button type="primary" @click="gotoLogin">登陆</el-button>
        <el-button type="primary">注册</el-button>
      </span>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
export default {
  data() {
    return {
      searchCriteria: "",
      breadcrumbItems: ["导航一"],
    };
  },

  methods: {
    handleIconClick(ev) {
      console.log(ev);
    },
    //跳转函数
    gotoLogin()
    {
      this.$router.replace('/login')
    }
  },
};
</script>

<style scoped>
#logo {
  color: white;
  float: left;
  padding-top: 18px;
  margin-left: 1%;
  font-size: 35px;
}
#login {
  float: right;
  margin: 15px;
}
#search {
  float: left;
  padding: 15px;
  color: white;
  margin-left: 2%;
  width: 15%;
}
</style>
