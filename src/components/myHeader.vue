<template>
    <div
      style="
        overflow: hidden;
		height: 60px;
		background-color: #3896C2;
      "
    >
      <span class="header" id="logo" @click="gotoHome"> FairMart </span>
      
      <div class="header" id="search">
        <div id="searchInput"><el-input
          placeholder="请输入"
          icon="search"
          v-model="searchCriteria"
          :on-icon-click="handleIconClick"
        >
        </el-input></div>
        <div id=searchButton><el-button  @click="switchPage()">搜索</el-button></div>
        
      </div>
      <span class="header" id="login">
        <div :is="currentView"></div>
      </span>
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
      currentView:GLOBAL.view,
      logined:GLOBAL.isLogined,
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
          if(this.logined==true) {
            this.currentView=MyCenter;
            GLOBAL.view=MyCenter;
          }
        }
      else {
        this.logined=false
        if(this.logined==false) {
          this.currentView=loginButton;
          GLOBAL.view=loginButton;
        }

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
  margin-left: 1%;
  font-size: 35px;
}
#login {
  float: right;
  margin-right: 1%;
  display: flex;
}
#search {
  float: left;
  padding: 5px;
  color: white;
  margin-left: 650px;
  width: 500px;
  position: relative;
  top:-5px;
  display: flex;
}
#searchButton{
  margin-left: 10px;
  display: inline-block;
  align-self: center;
}
#searchInput{
  width:300px;
  display: inline-block;
  align-self: center;
}
</style>
