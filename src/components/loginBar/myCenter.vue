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
            <el-menu-item index="2-1" @click="gotoMyGoods"
              >我发布的</el-menu-item
            >
            <el-menu-item index="2-2" @click="gotoMyPurchase">我拍下的</el-menu-item>
            <el-menu-item index="2-3" @click="gotoMyFavorite">我的收藏</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">这个菜单干什么好呢</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3" @click="dialog_changevx_Visible=true">更改联系方式</el-menu-item>
          <el-menu-item index="4" style="margin=0px;"
            ><a href="https://www.ele.me" target="_blank"
              >订单管理</a
            ></el-menu-item
          >
        </el-menu>
      </span>
    </span>
    <el-dialog
      :visible.sync="dialog_changevx_Visible"
      width="50%"
      style="text-align: center"
      
    >
      <span>请输入您的微信号</span>
      <el-input v-model="myWeChat"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialog_buying_Visible = false">取 消</el-button>
        <el-button type="primary" @click="changeMyWX">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import GLOBAL from "@/global/global";
import axios from "axios";
import Router from "../../router/index.js";
export default {
  data() {
    return {
      myWeChat:"",
      dialog_changevx_Visible: false,
    };
  },

  components: {},

  computed: {},

  mounted: {},

  methods: {
    gotoMyGoods() {
        Router.push({ path: '/myGoods', query: { type: "userallproducts" }});
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    changeMyWX() {
      if (this.myWeChat == "") {
        alert("请输入内容");
      }
      var vx=this.myWeChat;
      const  path="http://39.104.84.38:8080/changeWeChat";
      var WeChat_info={
        "user_id":GLOBAL.currentUser_ID,
        "WeChat_id":vx,
      }
      console.log(WeChat_info);
      var that=this;
      axios
					.post(path,JSON.stringify(WeChat_info))
					.then(function(response){
						var vx_result=response.data
						var vx_success = vx_result["result"];
						//alart(is_register_success)
						console.log(vx_success);//注意返回格式
						if(vx_success==="failed"){
							alert("登记失败，请重试");
						}else if(vx_success==="success"){
              //that.dialog_changevx_Visible=false;
              var alert_str="登记成功，您的微信为:"+vx;
							alert(alert_str);
              that.dialog_changevx_Visible=false;
						}else{
							alert("写个什么玩意？");
						}
					});
    },
    gotoMyPurchase(){
      console.log("goto my churse")
      Router.push({path:"myGoods",query:{type:"mypurchase"}});
    },
    gotoMyFavorite(){
      console.log("goto my favorite");
      Router.push({path:"myGoods",query:{type:"myfavorites"}});
    }
  },
};
</script>

<style>
.mycenter {
  float: right;
  margin: auto;
  height: 70px;
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