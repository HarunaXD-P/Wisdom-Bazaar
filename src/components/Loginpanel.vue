<template>
	<div class="panel">
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
				<el-button type="primary">
					登陆
				</el-button>
			</el-main>
			
			<el-footer style="margin-top: 200px;">
				<el-container>
					<el-link class="register" @click="registerlink">
						注册账号
					</el-link>
					
					<el-link class="findpassword" target="_blank" href="../findpassword/">
						找回密码
					</el-link>
				</el-container>
			</el-footer>
		</el-container>
	</div>
</template>

<script>
	export default{
		name: "Loginpanel",
		data(){
			return{
				active: 0,
				name: '',
				password: ''
			};
		},
		registerlink(){
			this.$router.push( {
				path:'../register'
			})
		},
	};
</script>

<style>
.panel{
	background-color:#40afe2;
	position: relative;
	margin-top: 300px;
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
