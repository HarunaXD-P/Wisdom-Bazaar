<template>
	<div id="app">
		<el-container>
			<el-header>
				<logo></logo>
			</el-header>
			<el-main style="align-self: center;">
				<body style="margin-top: 294px; font-size: 36px; margin-right: 0px;">
					注册新用户
				</body>
				<registerpanel></registerpanel> 
			</el-main>
		</el-container>
	</div>
</template>

<script>
import Logo from "@/components/Logo.vue";
import Registerpanel from "@/components/Registerpanel.vue"
import "element-ui/lib/theme-chalk/index.css";

export default {
  name: "App",
  components: {
	registerpanel: Registerpanel,
	logo: Logo,
  },
};
</script>

<style>
#app{
	font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	background-color: #3896C2;
	min-height:1080px;
}
</style>
