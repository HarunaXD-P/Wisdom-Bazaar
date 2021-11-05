<template>
	<div id="app">
		<el-container>
			<el-header>
				<logo></logo>
			</el-header>
			<el-main style="align-self: center;position:absolute;top:350px">
				<loginpanel></loginpanel> 
			</el-main>
		</el-container>
	</div>
</template>

<script>
import Logo from "@/components/Logo.vue";
import Loginpanel from "@/components/Loginpanel.vue"
import "element-ui/lib/theme-chalk/index.css";

export default {
  name: "App",
  components: {
	loginpanel: Loginpanel,
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
