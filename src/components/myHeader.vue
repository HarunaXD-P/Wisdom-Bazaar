<template>
  <div style="background-color: #ebebeb; min-height: 2000px; width:1920px; margin:auto">
    <div
      style="
        height: 61px;
        width: 1920px;
        background-color: #3896c2;
        overflow: hidden;
      "
    >
      <span class="header" id="logo"> FairMart </span>
      <div class="header" id="search">
        <div id="searchInput"><el-input
          placeholder="请输入"
          icon="search"
          v-model="searchCriteria"
          :on-icon-click="handleIconClick"
        >
        </el-input></div>
        <div id=searchButton><el-button  @click="getSearch">搜索</el-button></div>
        
      </div>
      <span class="header" id="login">
        <my-center></my-center>
      </span>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import loginButton from './loginBar/loginButton.vue';
import MyCenter from './loginBar/myCenter.vue';
export default {
  components: { loginButton, MyCenter },
  data() {
    return {
      searchCriteria: "",
      breadcrumbItems: ["导航一"],
    };
  },

  methods: {
    getSearch:function(){
      console.log(this.searchCriteria)

    },
    handleIconClick(ev) {
      console.log(ev);
    },
  },
};
</script>

<style scoped>
#logo {
  color: white;
  float: left;
  padding-top: 13px;
  margin-left: 1%;
  font-size: 35px;
}
#login {
  float: right;
  margin: auto;
  display: inline-block;
}
#search {
  float: left;
  padding: 15px;
  color: white;
  margin-left: 650px;
  width: 400px;
  position: relative;
  left:-95px;
  top:-3px;
}
#searchButton{
  margin:auto;
  display: inline-block;
}
#searchInput{
  width:300px;
  display: inline-block;
}
</style>
