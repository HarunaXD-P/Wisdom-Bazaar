<template>
  <div id="findpw">
    <div id="filler"></div>

    <div class="fp_layout">
      <div class="fp_left">
        <p>重置密码</p>
        <p>RESET PASSWORD</p>
      </div>

      <div class="fp_center">
        <div class="fp_form">
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
                <el-button
                  type="primary"
                  @click="check_email"
                  :loading="loadingbut"
                  >{{loadingtext}}</el-button
                >
              </el-col>
            </el-form-item>
            <!--
            <el-form-item label="用户名">
              <el-col :span="20">
                <el-input
                  placeholder="请输入用户名"
                  v-model="form.username"
                ></el-input>
              </el-col>
            </el-form-item>
			-->
            <el-form-item label="新密码">
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
                <el-button type="primary" @click="doResetpw">立即重置</el-button>
                <el-button type="primary" @click="gotoHome">返回主页</el-button>
              </el-col>
            </el-form-item>
          </el-form>
        </div>
      </div>

      <div class="fp_right">
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
import Findpasswordpanel from "@/components/Findpasswordpanel.vue";
import "element-ui/lib/theme-chalk/index.css";
import fair from "@/components/fairmart.vue";
import axios from "axios";
import crypto from "crypto";
import emailjs from "emailjs-com";
import apikeys from "../router/apikeys";
import "jquery";

export default {
  name: "Findpassword",
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
      loadingbut: false,
	    loadingtext:"发送验证码",
      msg: "",
      pw_md: "",
      random_vcode: "",
    };
  },
  methods: {
    gotoLogin() {
      this.$router.replace("/Login");
    },
	gotoHome(){
		this.$router.replace("/")
	},
    clearInput() {
      this.form.username = "";
      this.form.password = "";
      this.form.password_confirm = "";
      this.form.Email = "";
      this.form.vcode = "";
    },
	
    send_vcode() {
	
      this.loadingbut = true;
	    this.loadingtext="验证中"
	  //input is vcode,standard is random_vcode.
      var random6number = Math.random().toString().slice(-6);
      this.form.v_code = random6number;
      this.random_vcode = random6number;
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
	  var that=this;
      $.ajax("https://api.emailjs.com/api/v1.0/email/send", {
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
      })
        .done(function () {
          alert("邮件发送成功");
          that.loadingbut = false;
		      that.loadingtext = "发送成功";
        })
        .fail(function (error) {
          alert("Oops... " + JSON.stringify(error));
        });
		
    },
    test() {
      console.log(this.form.Email);
    },
    check_email() {
      var that = this;
      const path = "http://39.104.84.38:8080/Email_exist";
      var email_info = {
        "email": this.form.Email,
      };

      axios
        .post(path, JSON.stringify(email_info))
        .then(function (response) {
          var email_result = response.data["result"];
          console.log(email_result);
          if (email_result === "success") {
            that.send_vcode();
          } else {
            alert("邮箱不存在，请检查输入或重新注册");
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
	doResetpw(){
		if(this.form.password!=this.form.password_confirm){
			alert("两次输入密码不一致");
			return;
		}
		if(this.form.Email=="" || this.form.vcode==""){
			alert("请完成邮箱验证");
			return;
		}
		if(this.form.vcode!=this.random_vcode){
			alert("验证码错误，请重新输入");
			return;
		}
		var pw=this.form.password;
		var md5 = crypto.createHash("md5");
      	md5.update(pw); //this.pw2这是你要加密的密码
      	this.pw_md = md5.digest("hex");//加密完的pw_md
		var reset_info={
			"email":this.form.Email,
			"new_pw":this.pw_md,
		};
		const path="http://39.104.84.38:8080/resetpw"
		
		axios
		.post(path,JSON.stringify(reset_info))
		.then(function(response){
			var reset_result=response.data["result"];
			if(reset_result==="success"){
				alert("修改成功，请返回登录");
			}
			else{
				alert("修改失败，请重试");
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
		
	}
  },
};
</script>

<style>
#findpw {
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

.fp_layout {
  width: 900px;
  height: 450px;
  border: 5px solid #eeeeee;
  background-color: white;
  opacity: 0.8;
  /*让div水平居中*/
  margin: auto;
  margin-top: 20px;
}

.fp_left {
  float: left;
  margin: 15px;
  width: 20%;
}

.fp_left > p:first-child {
  color: #ffd026;
  font-size: 20px;
}

.fp_left > p:last-child {
  color: #a6a6a6;
}
.fp_center {
  /*border: 1px solid red;*/
  float: left;
  width: 450px;
  /*margin: 15px;*/
}

.fp_right {
  float: right;
  margin: 15px;
}

.fp_right > p:first-child {
  font-size: 15px;
}
.fp_right > p:last-child {
  font-size: 15px;
}

.fp_right p a {
  color: pink;
}
#filler {
  height: 20px;
}
</style>
