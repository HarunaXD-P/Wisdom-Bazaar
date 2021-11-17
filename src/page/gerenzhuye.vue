<!--el-container, 不会用，告辞-->
<template>
  <div id="app">
		<!--<Header> </Header>-->
		<div id="_selfinfo">
			<div id="_img">
				<img
					src="../assets/logo.jpg"
					width="200"
					height="150"
				/><img />
			</div>
			<div id="_idoth">
				<div id="_name"> Cai </div>
				<div id="_hitogoto"> 何も怖らず歩いて行こう</div>
			</div>
		</div>
		<div id="navfirst">
			<ul id="caimenu">
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 动态 </a>
				</li>
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 个人信息</a>
				</li>
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 个人信息</a>
				</li>
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 个人信息</a>
				</li>
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 个人信息</a>
				</li>
				<li id="c">
					<a href="http://www.baidu.com" title="个人信息"> 个人信息</a>
				</li>
			</ul>
		</div>
		<div id="dongtaiqu">
			<dongtai></dongtai>
		</div>
	</div>
</template>

<script>
import myHeader from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
import "element-ui/lib/theme-chalk/index.css";
import _first from "@/components/cai_msg"

export default {
  name: "App",
  components: {
    Header: myHeader,
    myLeftSidebar: LeftSidebar,
    myDisplay: DisplaySix,
    myInfirmation: information,
		dongtai: _first,
  },
};
</script>

<style>
	
#_selfinfo {
	height: 150px;
	width: 1800px;
}
	
#_img {
	height: 150px;
	width: 200px;
	margin: 0px;
	padding-top: 0px;
	border: 0px;
	background: none;
	float: left;
}

#_idoth {
	height: 150px;
	width: 1600px;
	margin: 0px, 20px;
	float: left;
}

#_name {
	height: 50px;
	font-size: 35px;
	text-align: left;
	position: relative;
	top: 50px;
}

#_hitogoto {
	height: 25px;
	font-size: 15pt;
	text-align: left;
	position: relative;
	top: 50px;
}
	
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-right : 0px;
  width:1920px;
  height:1080px;
  float:center;
  margin:auto;
}

#navfirst {
	height: 48px;
	width: 1800px;
	padding-top: 0px;
	margin-left: 20px;
	border: 0px;
	background: #E8E7E3;
}

#caimenu {
	padding: 0px;
	position: relative;
	text-align: center;
}

#c {
	height: 48px;
	width: 300px;
	list-style: none;
	float: left;
	font-size: 30px;
}

#dongtaiqu {
	width: 1800px;
	margin-top: 20px;
	margin-left: 20px;
	min-height: 800px;
}


</style>
