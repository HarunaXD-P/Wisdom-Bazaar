<template>
  <div style="background-color: #ebebeb; min-height: 0px; width:1920px; margin:auto">
    <div
      style="
        height: 61px;
        width: 1920px;
        background-color: #3896c2;
        overflow: hidden;
      "
    >
      <span class="header" id="logo" @click="gotoHome"> FairMart </span>
      <!--
      <div class="header" id="search">
        <div id="searchInput"><el-input
          placeholder="请输入"
          icon="search"
          v-model="searchCriteria"
          :on-icon-click="handleIconClick"
        >
        </el-input></div>
        <div id=searchButton><el-button  @click="switchPage()">搜索</el-button></div>
        
      </div>-->
      <span class="header" id="login">
        <div :is="currentView"></div>
      </span>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import loginButton from './loginBar/loginButton.vue';
import MyCenter from './loginBar/myCenter.vue';
import GLOBAL from '@/global/global'
export default {
  components: { loginButton, MyCenter },
  data() {
    return {
      searchCriteria: "",
      breadcrumbItems: ["导航一"],
      currentView:'loginButton',
      logined:GLOBAL.logined,
    };
  },

  methods: {
    getSearch:function(){
      console.log(this.searchCriteria)
    },
    handleIconClick(ev) {
      console.log(ev);
    },
    switchPage()
    {
      if(this.logined==false)
        {
          this.logined=true
          if(this.logined==true) this.currentView=MyCenter
        }
      else {
        this.logined=false
        if(this.logined==false) this.currentView=loginButton

      }
    },
    gotoHome()
    {
      this.$router.replace('/')
    }
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
