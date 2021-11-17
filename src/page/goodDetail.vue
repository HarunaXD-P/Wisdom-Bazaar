<!-- el-container, 不会用，告辞-->
<!-- 基本写法是利用 float 设置悬浮，然后控制容器的大小来控制其位置，
     优点是只要有了图基本都能在网页上较快地实现，缺点是不好维护
 -->
<template>
  <div id="app">
		<Header> </Header>
		<div id="cai_good_detail">
			<ul id="caimenu">
				<!-- 这四个超链接暂时先这样凑活一下，以后要改 -->
				<li id="caimenu_sy">
					<a href="http://www.baidu.com" title="首页"> 首页 </a>
				</li>
				<li id="caimenu_sc">
					<a href="http://www.baidu.com" title="商城"> 商城 </a>
				</li>
				<li id="caimenu_qg">
					<a href="http://www.baidu.com" title="求购"> 求购 </a>
				</li>
				<li id="caimenu_lxwm">
					<a href="http://www.baidu.com" title="联系我们"> 联系我们</a>
				</li>
			</ul>
		</div>
		<div id="cai_detail_box">
			<div style="height: 640px">
				<!-- 这里放商品详情框上面的部分 -->
				<div style="width: 684px; height: 464px; float: left">
					<!-- 这里放图片 -->
					<img
						src="../assets/iphone.jpeg"
						width="684px"
						height="464px"
					/><img />
				</div>
				<div style="width: 386px; height: 71px; margin-left: 64px; font-size: 48px; float: left">
					崭新iPhone13Pro
				</div>
				<div style="width: 299px; height: 30px; margin-left: 66px; font-size: 20px; color: red; float: left">
					苹果手机 电子产品 三摄像头IP68
				</div>
				<div style="width: 412px; height: 71px; margin-left: 64px; font-size: 48px; float: left">
					<p style="margin: 0px; padding: 0px; color: gray; float: left"> 价格 </p>
					<p style="margin: 0px; padding: 0px; color: red; float: right"> ￥7229 </p>
				</div>
				
				<!-- 画一条横线 -->
				<div style="height: 10px; width: 499px; margin-left: 42px; float: left"> <hr /> </div>
				<div style="width: 216px; height: 106px; margin-left: 41px; margin-top: 59px; float: left;
										font-size: 36px; color: rgba(181, 161, 161, 1)">
					方便交易时间<br> 全天
				</div>
				<!-- 画一条竖线 -->
				<div style="width: 10px; height: 176px; margin-left: 35px; margin-top: 24px; float: left;
										border-left: 1px solid rgba(166, 166, 166, 1);">
				</div>					
				<div style="width: 216px; height: 106px; margin-left: 25px; margin-top: 59px; float: left;
										font-size: 36px; color: rgba(181, 161, 161, 1)">
					剩余有效期<br> 30天
				</div>
				<!-- 画一条横线 -->
				<div style="height: 10px; width: 499px; margin-left: 42px; margin-top: 31px; float: left"> <hr /> </div>
				
				<!-- 下面还有两个按钮 -->
				<div style="height: 130px; width: 535px; margin-left: 42px; margin-top: 42px; float: left">
					<button type="button" style="height: 130px; width: 240px;  float: left;
					  font-size: 48px; background-color: rgba(255, 77, 79, 1); border-radius: 15px; color: white"> 
						立即联系
					</button>
					<button type="button" style="height: 130px; width: 240px; margin-left: 20px; float: left;
					  font-size: 48px; background-color: rgba(232, 169, 132, 1); border-radius: 15px; color: white"> 
						加购物车
					</button>
				</div>
			</div>	
			
			<div>
				<!-- 这里放 商品详情 文字部分 -->
				<!-- 字体什么的，以后再管了 -->
				<div style="height: 119px; width: 100%; float: left; background-color: rgba(196, 196, 196, 1); ">
					<p style="margin: 0px 0px 0px 35px; padding: 0px; color: white; float: left; 
					  font-size: 48px; line-height: 119px">
						商品详情 
					</p>
				</div>
				<div style="min-height: 118px; width: 100%; float: left;">
					<p style="margin: 10px 0px 0px 41px; padding: 0px; float: left; font-size: 36px;
						text-align: left; color: rgba(120, 66, 66, 1)">
						据介绍，iPhone13Pro正面采用一块6.1英寸的OLED屏，屏幕刷新率120Hz，支持1Hz至120Hz刷新率调节，
						屏幕分辨率2532X1170，机身厚度7.65mm，重203g。 拍照上，Pro版本后置采用三颗1200万像素的镜头，
						1200万像素广角，1200万像素超广角，和1200万像素长焦，支持3倍光学变焦，15倍数码变焦。 
						广角镜头和长焦镜头都支持光学防抖。
					</p>
				</div>
			</div>
		</div>
		<div style="float: right">
			<myInfirmation> </myInfirmation>
		</div>
	</div>
</template>

<script>
import myHeader from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
//import "element-ui/lib/theme-chalk/index.css";
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

#cai_good_detail{
	height: 48px;
	width: 1120px;
	padding-top: 0px;
	margin-left: 400px;
	border: 0px;
	background: #E8E7E3;
}

#caimenu {
	padding: 0px;
	position: relative;
	text-align: center;
}

#caimenu_sy {
	height: 48px;
	width: 280px;
	list-style: none;
	float: left;
	font-size: 30px;
}

#caimenu_sc {
	height: 48px;
	width: 280px;
	list-style: none;
	float: left;
	font-size: 30px;
}

#caimenu_qg {
	height: 48px;
	width: 280px;
	list-style: none;
	float: left;
	font-size: 30px;
}

#caimenu_lxwm {
	height: 48px;
	width: 280px;
	list-style: none;
	float: left;
	font-size: 30px;
}

#cai_detail_box {
	width: 1261px;
	mim-height: 880px;
	margin-left: 256px;
	margin-top: 30px;
	float: left;
}


</style>
