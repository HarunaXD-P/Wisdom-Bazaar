<template>
	<div class="loginpanel">
		<el-container>
			<el-main>
				<body class="username">
					用户名
				</body>
				
				<el-input style="margin-top: 50px;" clearable v-model="name">
				</el-input>
				
				<body class="password">
					密码
				</body>
				
				<el-input style="margin-top: 90px;" show-password v-model="password">
				</el-input>
				
				<el-container>
					<el-checkbox class="rememberme">
						记住我
					</el-checkbox>
				</el-container>
				<el-button type="primary" style="position:absolute;top:350px;left:150px" @click="checkLogin">
					登陆
				</el-button>
				<el-button type="primary" style="position:absolute;top:350px;left:350px" @click="gotoHome">
					返回
				</el-button>
			</el-main>
			
			<el-footer style="margin-top: 200px;">
				<el-container>
					<el-link class="register" @click="registerlink">
						注册账号
					</el-link>
					
					<el-link class="findpassword" @click="findpasswordlink">
						找回密码
					</el-link>
				</el-container>
			</el-footer>
		</el-container>
	</div>
</template>

<script>
	import GLOBAL from '@/global/global'
	import crypto from 'crypto'
	import axios from 'axios'
	export default{
		name: "Loginpanel",
		data(){
			return{
				active: 0,
				name: '',
				password: '',
				pw_md:''
			};
		},
		methods:{
			registerlink(){
				this.$router.replace('/register')
			},
			findpasswordlink(){
				this.$router.replace('/findpassword')
			},
			gotoHome(){
				this.$router.replace('/')
			},
			checkLogin(){
				//var userJson=JSON.parse(GLOBAL.j_str);
				var pw=this.password;
				var is_login_success;
				var md5 = crypto.createHash("md5");
				md5.update(pw);//this.pw2这是你要加密的密码
				this.pw_md = md5.digest('hex');//this.pw这就是你加密完的密码，这个往后台传就行了
				console.log(this.pw_md);
				/*
				if(this.name==userJson.username){
					if(this.pw_md==userJson.password){
						alert("登陆成功");
						this.$router.replace('/')
						GLOBAL.view="myCenter";

					}else{
						alert("密码错误")
						this.name='';
						this.password='';
						return;
					}
				}else{
					alert("用户名错误");
					this.name='';
					this.password='';
					return;
				}
				*/
				var loginInfo={
					"user_name":this.name,
					"password":this.pw_md,
				}
				const  path="http://127.0.0.1:5000/login";
				axios
					.post(path,JSON.stringify(loginInfo))
					.then(function(response){
						console.log("i accept")
						var login_result=response.data;
						is_login_success=login_result["result"];
						if(is_login_success==="success"){
							alert("登陆成功");
							GLOBAL.currentUser_ID=login_result["id"];
							GLOBAL.currentUser_name=login_result["user_name"];
							GLOBAL.isLogined=true;
							GLOBAL.view="myCenter";
							GLOBAL.isLogined=true;
						}else if(is_login_success==="failed"){
							alert("登陆失败")
							this.name="";
							this.password="";
						}else{
							alert("传参失败");
						}
					})
				
				
				
			}
		},
	};
</script>

<style>
.loginpanel{
	background-color:#40afe2;
	position: relative;
	margin-top: 30px;
	width: 594px;
	height: 520px;
}
.username{
	font-size:24px;
	position: absolute;
}
.password{
	font-size:24px;
	position: absolute;
	margin-top:50px;
}
.rememberme{
	position:absolute;
	margin-top: 30px;
	margin-left: 10px;
}
.register{
	position: absolute;
	margin-left: 10px;
}
.findpassword{
	position: absolute;
	margin-left: 430px;
}
</style>
