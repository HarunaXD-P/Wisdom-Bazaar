<template>
	<div id="app">
		<div class="rg_layout">
			<div class="rg_left">
				<p>新用户注册</p>
				<p>USER REGISTER</p>
			</div>

			<div class="rg_center">
			<div class="rg_form">
				<div style="margin: 50px 0;"></div>
				<el-form ref="form" :model="form" :rules="rules" label-width="80px">
				<el-form-item label="Email" prop="Email">
					<el-col :span="15">
					<el-input placeholder="请输入邮箱号" v-model="form.Email"></el-input>
					</el-col>
					<el-col :span="9">
					<el-button type="success" plain @click="sendEmail">发送邮件验证</el-button>
					</el-col>
				</el-form-item>
				<el-form-item label="用户名">
					<el-col :span="20">
					<el-input placeholder="请输入用户名" v-model="form.username"></el-input>
					</el-col>
				</el-form-item>
				<el-form-item label="密码">
					<el-input placeholder="请输入密码" v-model="form.password"></el-input>
				</el-form-item>
				<el-form-item label="确认密码">
					<el-input placeholder="请输入密码" v-model="form.password"></el-input>
				</el-form-item>

				<el-form-item label="验证码">
					<el-col :span="15">
					<el-input
						type="text"
						placeholder="验证码将会发送到您的邮箱"
						v-model="form.text"
						oninput="value=value.replace(/\D/g,'')"
						maxlength="6"
						show-word-limit
					>
					</el-input>
					</el-col>
				</el-form-item>
				<el-form-item>
					<el-col :span="20">
					<el-button type="primary" @click="onSubmit">立即注册</el-button>
					</el-col>
				</el-form-item>
				</el-form>
			</div>
			</div>

			<div class="rg_right">
      			<p>已有账号?
        		<el-link icon="el-icon-user-solid" type="primary" @click="login_asd">立刻登陆</el-link>
      			</p>
    		</div>

		</div>

	</div>
</template>

<script>
import Logo from "@/components/Logo.vue";
import Registerpanel from "@/components/Registerpanel.vue"
import "element-ui/lib/theme-chalk/index.css";
import fair from "@/components/fairmart.vue";

export default {
  name: "App",
  components: {
	registerpanel: Registerpanel,
	logo: Logo,
	fairmart: fair,
  },
   data: function () {
    return {
      form: {
        Email: '',
        username: "",
        password: "",
        radio: '1',
        date: '',
        text: ''
      },
      rules: {
        Email: [{required: true, message: '请输入邮箱', trigger: 'blur'}]
      },
      msg: ''
    }
   }

};
</script>

<style>
#app{
	font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	
	min-height:1080px;
}
body {
  background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgs.aixifan.com%2Fo_1cp6p00oj12fi1i6m1k1515ef1ov97s.png&refer=http%3A%2F%2Fimgs.aixifan.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641108632&t=fa99d09a6f167c737161bdb9e6dc2efb);
  background-repeat: no-repeat;
  background-size: 100%;
  background-position: 0px -50px;
}

.rg_layout {
  width: 900px;
  height: 450px;
  border: 5px solid #EEEEEE;
  background-color: white;
  opacity: 0.8;
  /*让div水平居中*/
  margin: auto;
  margin-top: 200px;
}
.rg_left {
  float: left;
  margin: 15px;
  width: 20%;
}
.rg_left > p:first-child {
  color: #FFD026;
  font-size: 20px;
}

.rg_left > p:last-child {
  color: #A6A6A6;
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

.rg_center {
  /*border: 1px solid red;*/
  float: left;
  width: 450px;
  /*margin: 15px;*/
}

</style>
