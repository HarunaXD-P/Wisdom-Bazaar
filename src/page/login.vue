<template>
  <div id="Login">
    <div id="filler"></div>
    <!--
		<el-container>
			<fairmart></fairmart>
			<el-header>
				<logo></logo>
			</el-header>
			<el-main style="align-self: center;margin-top:270px">
				<loginpanel></loginpanel> 
			</el-main>
		</el-container>
		-->
    <div class="lg_layout">
      <div class="lg_left">
        <p>用户登录</p>
        <p>USER LOGIN</p>
      </div>

      <div class="lg_center">
        <div class="lg_form">
          <div style="margin: 50px 0"></div>
          <el-form ref="form" :model="form" :rules="rules" label-width="80px">
            <el-form-item label="用户名">
              <el-col :span="20">
                <el-input
                  placeholder="请输入用户名"
                  v-model="form.username"
                ></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="密码">
              <el-input
                placeholder="请输入密码"
                v-model="form.password"
                show-password
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-col :span="20">
                <el-button type="primary" @click="doLogin">立即登陆</el-button>
                <el-button type="primary" @click="gotoHome">返回主页</el-button>
              </el-col>
            </el-form-item>
          </el-form>
        </div>
      </div>

      <div class="lg_right">
        <p>
          未拥有账号?
          <el-link
            icon="el-icon-user-solid"
            type="primary"
            @click="gotoRegister"
            >立刻注册</el-link
          >
        </p>
        <p>
          忘记密码？
          <el-link
            icon="el-icon-s-release"
            @click="gotoFindpw"
          >重置密码</el-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from "@/components/Logo.vue";
//import Loginpanel from "@/components/Loginpanel.vue"
import "element-ui/lib/theme-chalk/index.css";
//import fair from "@/components/fairmart.vue";
import axios from "axios";
import crypto from "crypto";
import GLOBAL from "@/global/global";

export default {
  name: "Login",
  components: {
    //loginpanel: Loginpanel,
    logo: Logo,
    //fairmart: fair,
  },
  data: function () {
    return {
      form: {
        username: "",
        password: "",
      },
      rules: {
        Email: [{ required: true, message: "请输入邮箱", trigger: "blur" }],
      },
      msg: "",
      pw_md: "",
    };
  },
  methods: {
    gotoRegister() {
      this.$router.replace("/Register");
    },
    gotoFindpw(){
      this.$router.replace("/Findpassword")
    },
    gotoHome() {
      this.$router.push({ path: "/", query: { from: "login" } });
    },
    doLogin() {
		if(this.form.username=="" || this.form.password==""){
			alert("请输入账号密码");
      return;
		}
      var pw = this.form.password;
      var is_login_success;
      var md5 = crypto.createHash("md5");
      md5.update(pw); //this.pw2这是你要加密的密码
      this.pw_md = md5.digest("hex"); //this.pw这就是你加密完的密码，这个往后台传就行了
      console.log(this.pw_md);

      var loginInfo = {
        user_name: this.form.username,
        password: this.pw_md,
      };
      const path = "http://39.104.84.38:8080/login";
      axios.post(path, JSON.stringify(loginInfo)).then(function (response) {
        console.log("i accept");
        var login_result = response.data;
        is_login_success = login_result["result"];
        if (is_login_success === "success") {
          alert("登陆成功");
          GLOBAL.currentUser_ID = login_result["id"];
          GLOBAL.currentUser_name = login_result["user_name"];
          GLOBAL.isLogined = true;
          GLOBAL.view = "myCenter";
          GLOBAL.isLogined = true;
        } else if (is_login_success === "failed") {
          alert("登陆失败");
          this.name = "";
          this.password = "";
        } else {
          alert("传参失败");
        }
      });
    },
  },
};
</script>

<style>
#Login {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  max-width: 1100px;
  min-height: 900px;
  margin: auto;
  background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgs.aixifan.com%2Fo_1cp6p00oj12fi1i6m1k1515ef1ov97s.png&refer=http%3A%2F%2Fimgs.aixifan.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641175021&t=4251d39d1a838bdc8d06c5a3b4c7b4fc);
  background-repeat: no-repeat;
  background-size: 100%;
  background-position: 0px -50px;
}

* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

.lg_layout {
  width: 900px;
  height: 300px;
  border: 5px solid #eeeeee;
  background-color: white;
  opacity: 0.8;
  /*让div水平居中*/
  margin: auto;
  margin-top: 0px;
}

.lg_left {
  float: left;
  margin: 15px;
  width: 20%;
}
.lg_left > p:first-child {
  color: #ffd026;
  font-size: 20px;
}

.lg_left > p:last-child {
  color: #a6a6a6;
}

.lg_center {
  /*border: 1px solid red;*/
  float: left;
  width: 450px;
  /*margin: 15px;*/
}

.lg_right {
  float: right;
  margin: 15px;
}

.lg_right > p:first-child {
  font-size: 15px;
}

.lg_right p a {
  color: pink;
}

#filler {
  height: 50px;
}
</style>
