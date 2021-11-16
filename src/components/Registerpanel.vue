<template>
	<div class="panel">
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
				this.$router.go(0)
			},
			printReg(){
				console.log(this.name);
				console.log(this.password);
			},
			doRegist(){
				var pw=this.password;
				var pwc=this.passwordconfirm;

				if(pw!=pwc){
					alert("输入密码不一致，请重新输入");
					this.name="";
					this.password="";
					this.passwordconfirm="";
				}//检验两次输入是否一致，明文

				var md5 = crypto.createHash("md5");
				md5.update(pw);//this.pw2这是你要加密的密码
				this.pw_md = md5.digest('hex');//this.pw这就是你加密完的密码，这个往后台传就行了

				var j={};
				j.username=this.name;
				j.password=this.pw_md;
				j.email=this.email;//写入json


				this.j_str=JSON.stringify(j);
				console.log(j_str);
				this.exportJSON;
			},
			exportJSON () {
			// 将json转换成字符串
			//const data = JSON.stringify(this.CfgInfo)
			const blob = new Blob([j_str], {type: ''})
			FileSaver.saveAs(blob, 'hahaha.json')
			}

		},
	};
</script>

<style>
.panel{
	background-color:#40afe2;
	position: relative;
	margin-top: 30px;
	width: 594px;
	height: 670px;
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
