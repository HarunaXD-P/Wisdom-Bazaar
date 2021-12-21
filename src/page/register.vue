<template>
  <div id="Register">
    <div id="filler"></div>
    <!--
		<el-container>
			<fairmart></fairmart>
			<el-header>git
				<logo></logo>
			</el-header>
			<el-main style="align-self: center;">
				<body style="margin-top: 214px; font-size: 36px; margin-right: 0px;">
					注册新用户
				</body>
				<registerpanel></registerpanel> 
			</el-main>
		</el-container>
		-->
    <div class="rg_layout">
      <div class="rg_left">
        <p>新用户注册</p>
        <p>USER REGISTER</p>
      </div>

      <div class="rg_center">
        <div class="rg_form">
          <div style="margin: 50px 0"></div>
          <el-form
            ref="form"
            :model="form"
            :rules="rules"
            label-width="80px"
            @submit.prevent="send_vcode"
          >
            <el-form-item label="Email" prop="Email">
              <el-col :span="15">
                <el-input
                  placeholder="请输入邮箱号"
                  v-model="form.Email"
                ></el-input>
              </el-col>
              <el-col :span="9">
                <el-button type="primary" 
                @click="send_vcode"
                :loading="rg_loadingbut"
                  >{{rg_loadingtext}}</el-button
                >
              </el-col>
            </el-form-item>
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
            <el-form-item label="确认密码">
              <el-input
                placeholder="请确认密码"
                v-model="form.password_confirm"
                show-password
              ></el-input>
            </el-form-item>
            <el-form-item label="验证码">
              <el-col :span="15">
                <el-input
                  type="text"
                  placeholder="验证码将会发送到您的邮箱"
                  v-model="form.vcode"
                  oninput="value=value.replace(/\D/g,'')"
                  maxlength="6"
                  show-word-limit
                >
                </el-input>
              </el-col>
            </el-form-item>
            <el-form-item>
              <el-col :span="20">
                <el-button type="primary" @click="doRegist">立即注册</el-button>
                <el-button type="primary" @click="gotoHome">返回主页</el-button>
              </el-col>
            </el-form-item>
          </el-form>
        </div>
      </div>

      <div class="rg_right">
        <p>
          已有账号?
          <el-link icon="el-icon-user-solid" type="primary" @click="gotoLogin"
            >立刻登陆</el-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from "@/components/Logo.vue";
//import Registerpanel from "@/components/Registerpanel.vue"
import "element-ui/lib/theme-chalk/index.css";
//import fair from "@/components/fairmart.vue";
import axios from "axios";
import crypto from "crypto";
import emailjs from "emailjs-com";
import apikeys from "../router/apikeys";
import "jquery";

export default {
  name: "Register",
  components: {
    //registerpanel: Registerpanel,
    logo: Logo,
    //fairmart: fair,
  },
  data: function () {
    return {
      form: {
        Email: "",
        username: "",
        password: "",
        password_confirm: "",
        //radio: '1',
        //date: '',
        vcode: "",
        v_code: "",
      },
      rules: {
        Email: [{ required: true, message: "请输入邮箱", trigger: "blur" }],
      },
      msg: "",
      pw_md: "",
      random_vcode: "",
      rg_loadingbut: false,
	    rg_loadingtext:"发送验证码",
    };
  },
  methods: {
    gotoHome() {
      this.$router.push({ path: "/", query: { from: "register" } });
    },
    gotoLogin() {
      this.$router.replace("/Login");
    },
    printReg() {
      console.log(this.form.username);
      console.log(this.form.password);
    },
    clearInput() {
      this.form.username = "";
      this.form.password = "";
      this.form.password_confirm = "";
      this.form.Email = "";
      this.form.vcode = "";
    },
    send_vcode() {
      var random6number = Math.random().toString().slice(-6);
      this.form.v_code = random6number;
      this.random_vcode = random6number;
      this.rg_loadingbut = true;
	    this.rg_loadingtext="验证中"
      console.log(random6number);

      var data = {
        service_id: apikeys.SERVICE_ID,
        template_id: apikeys.TEMPLATE_ID,
        user_id: apikeys.USER_ID,
        template_params: {
          Email: this.form.Email,
          v_code: random6number,
        },
      };
      $.ajax("https://api.emailjs.com/api/v1.0/email/send", {
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
      })
        .done(function () {
          alert("邮件发送成功");
          that.rg_loadingbut = false;
		      that.rg_loadingtext = "发送成功";
        })
        .fail(function (error) {
          alert("Oops... " + JSON.stringify(error));
        });
    },
    doRegist() {

      if (
        this.form.username == "" ||
        this.form.password == "" ||
        this.form.password_confirm == ""
      ) {
        alert("请完整填写信息");
        return;
      }
      if (this.form.Email == "") {
        alert("请填写邮箱");
        return;
      }
      
      var pw = this.form.password;
      var pwc = this.form.password_confirm;
      const path = "http://39.104.84.38:8080/register";
      var is_register_success;

      if (pw != "" && pw != pwc) {
        alert("输入密码不一致，请重新输入");
        clearInput();
        return;
      } //检验两次输入是否一致，明文
      if (this.form.vcode != this.random_vcode) {
        alert("验证码错误，请重新输入");
        this.form.vcode = "";
        return;
      }

      var md5 = crypto.createHash("md5");
      md5.update(pw); //this.pw2这是你要加密的密码
      this.pw_md = md5.digest("hex"); //this.pw这就是你加密完的密码，这个往后台传就行了

      var regist_info = {
        user_name: this.form.username,
        password: this.pw_md,
        email: this.form.Email,
      };

      axios
        .post(path, JSON.stringify(regist_info))
        .then(function (response) {
          var login_result = response.data;
          is_register_success = login_result["result"];
          //alart(is_register_success)
          console.log(is_register_success);
          if (is_register_success === "failed") {
            alert("注册失败，请重试");
            this.clearInput();
          } else if (is_register_success === "success") {
            alert("注册成功");
          } else {
            alert("传了个什么玩意？");
          }
        })
        .catch((error) => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    },
  },
  data: function () {
    return {
      form: {
        Email: "",
        username: "",
        password: "",
        radio: "1",
        date: "",
        text: "",
      },
      rules: {
        Email: [{ required: true, message: "请输入邮箱", trigger: "blur" }],
      },
      msg: "",
    };
  },
};
</script>

<style>
#Register {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /*background-color: #3896C2;*/
  /*min-height:1080px;*/
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

.rg_layout {
  width: 900px;
  height: 450px;
  border: 5px solid #eeeeee;
  background-color: white;
  opacity: 0.8;
  /*让div水平居中*/
  margin: auto;
  margin-top: 20px;
}

.rg_left {
  float: left;
  margin: 15px;
  width: 20%;
}

.rg_left > p:first-child {
  color: #ffd026;
  font-size: 20px;
}

.rg_left > p:last-child {
  color: #a6a6a6;
}
.rg_center {
  /*border: 1px solid red;*/
  float: left;
  width: 450px;
  /*margin: 15px;*/
}

.rg_right {
  float: right;
  margin: 15px;
}

.rg_right > p:first-child {
  font-size: 15px;
}

.rg_right p a {
  color: pink;
}
#filler {
  height: 20px;
}
/*
body {
  background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgs.aixifan.com%2Fo_1cp6p00oj12fi1i6m1k1515ef1ov97s.png&refer=http%3A%2F%2Fimgs.aixifan.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641108632&t=fa99d09a6f167c737161bdb9e6dc2efb);
  background-repeat: no-repeat;
  background-size: 100%;
  background-position: 0px -50px;
}
*/
</style>
