<template>
	<div class="findpasswordpanel">
		<el-container>
			<el-main>
				<body class="email">邮箱</body>
				
				<el-input style="margin-top: 50px;"></el-input>
				
				<body class="vcode">验证码</body>
				
				<el-input style="margin-top: 50px;"></el-input>
				
				<body class="newpassword">新密码</body>
				
				<el-input style="margin-top: 50px;"></el-input>
				
				<body class="passwordconfirm">确认密码</body>
				
				<el-input style="margin-top: 50px;"></el-input>
				
			</el-main>
			
			<el-footer>
				<el-button type="primary">
					修改
				</el-button>
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
			};
		},
	};
</script>

<style>
.findpasswordpanel{
	background-color:#40afe2;
	position: relative;
	margin-top: 30px;
	width: 594px;
	height: 600px;
}
.email{
	font-size:24px;
	position: absolute;
}
.vcode{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
.newpassword{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
.passwordconfirm{
	font-size:24px;
	position: absolute;
	margin-top:10px;
}
</style>
