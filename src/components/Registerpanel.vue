<template>
	<div class="registerpanel">
		<el-container>
			<el-main>
				<body class="username">用户名</body>
				
				<el-input style="margin-top: 50px;" clearable v-model="name">
				</el-input>
				
				<body class="password">密码</body>
				
				<el-input style="margin-top: 50px;" show-password v-model="password">
				</el-input>
				
				<body class="passwordconfirm">确认密码</body>
				
				<el-input style="margin-top: 50px;" show-password v-model="passwordconfirm">
				</el-input>
				
				<body class="email">邮箱</body>
				
				<el-input style="margin-top: 50px;" clearable v-model="email">
				</el-input>
				
				<body class="vcode">验证码</body>
				
				<el-input style="margin-top: 50px;" v-model="vcode"></el-input>
			</el-main>
			
			<el-footer>
				<el-button type="primary" id="registerButton" @click="doRegist">
					注册
				</el-button>
				<el-button type="primary" @click="gotoHome">
					返回
				</el-button>
			</el-footer>
			
		</el-container>
	</div>
</template>

<script>
	import crypto from 'crypto'
	import FileSaver from 'file-saver'
	import GLOBAL from '@/global/global'
	import axois from 'axios'
	export default{
		name: "Registerpanel",
		data(){
			return{
				active: 0,
				name: '',
				password: '',
				passwordconfirm: '',
				email: '',
				vcode: '',
				pw_md:'',
				j_str:'',
			};
		},
		methods:{
			gotoHome(){
				this.$router.replace('/')
				//this.$router.go(0)
			},
			gotoLogin(){
				this.$router.replace('/Login')
			},
			printReg(){
				console.log(this.name);
				console.log(this.password);
			},
			clearInput(){
				this.name="";
				this.password="";
				this.passwordconfirm="";	
				this.email="";
				this.vcode="";
			},
			doRegist(){
				
				var pw=this.password;
				var pwc=this.passwordconfirm;
				const path = "http://127.0.0.1:5000/register";
				var is_register_success;

				if(pw!=pwc){
					alert("输入密码不一致，请重新输入");
					this.name="";
					this.password="";
					this.passwordconfirm="";
				}//检验两次输入是否一致，明文

				var md5 = crypto.createHash("md5");
				md5.update(pw);//this.pw2这是你要加密的密码
				this.pw_md = md5.digest('hex');//this.pw这就是你加密完的密码，这个往后台传就行了
				
				var regist_info={
					"user_name":this.name,
					"password":this.pw_md,
				};
				//暂时不写邮箱了
				//j.email=this.email;//写入json

				/*
				this.j_str=JSON.stringify(j);
				//console.log(this.j_str);

				GLOBAL.j_str=this.j_str;
				console.log(GLOBAL.j_str);
				*/
				axois
					.post(path,JSON.stringify(regist_info))
					.then(function(response){
						var login_result=response.data
						is_register_success = login_result["result"];
						//alart(is_register_success)
						console.log(is_register_success);
						if(is_register_success==="failed"){
							alert("注册失败，请重试");
							this.clearInput();
						}else if(is_register_success==="success"){
							alert("注册成功");
						}else{
							alert("传了个什么玩意？");
						}
					});
				


			},
			// 导出生成json文件
     		downloadJson(data) {
         		var blob = new Blob([JSON.stringify(data)], { type: "" });
         		FileSaver.saveAs(blob, "hello.json");
     		},

		},
	};
</script>

<style>
.registerpanel{
	background-color:#40afe2;
	position: relative;
	margin-top: 30px;
	width: 594px;
	height: 600px;
}
.username{
	font-size:24px;
	position: absolute;
}
.password{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
.passwordconfirm{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
.email{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
.vcode{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
#registerButton{
	margin-top:50px;
}
</style>
