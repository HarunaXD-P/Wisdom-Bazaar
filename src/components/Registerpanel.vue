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
				<el-button type="primary" id="registerButton">
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
	export default{
		name: "Registerpanel",
		data(){
			return{
				active: 0,
				name: '',
				password: '',
				passwordconfirm: '',
				email: '',
				vcode: ''
			};
		},
		methods:{
			gotoHome(){
				this.$router.replace('/')
				this.$router.go(0)
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
