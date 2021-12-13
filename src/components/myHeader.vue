<template>
    <div id="header_panel">
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
#header_panel {
	background-color: #3896C2;
	height: 60px;
	line-height: 60px;
	text-align: center;
	display: flex;
}
#logo {
  color: white;
  float: left;
  margin-left: 10px;
  font-size: 35px;
}
#login {
  float: right;
  /*
  margin-left: 200px;
  display: flex;
  */
  
  margin:auto;
  margin-right:25px;
}
#search {
  float: left;
  color: white;
	margin: auto;
	/*margin-left: 300px;*/
  width: 500px;
  position: relative;
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
