<!--这个文件可以理解成一个整体显示的效果，主要是将其余个组件放在一个网页中-->
<template>
  <div id="tagpage">
    <!--整个显示出来的是一个面板，看效果还很不好，之后要改-->
    <router-view/>
    <el-container class="panel">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header id="header">
        <myHeader> </myHeader>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main style="padding: unset;">
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container class="el-main-panel">
          <myLeftSidebar></myLeftSidebar>
          <div>
				<body>
					分类：{{tag_name()}}
				</body>
			    <myDisplay v-bind:searchtag = "search_tag"></myDisplay>
		  </div>
          <myInformation></myInformation>
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
import GLOBAL from '@/global/global';
import axios from "axios";
import "element-ui/lib/theme-chalk/index.css";
export default {
  name: "Tagpage",
  components: {
    myHeader: Header,
    myLeftSidebar: LeftSidebar,
    myDisplay: DisplaySix,
    myInformation: information,
  },
  data(){
	  return{
		  search_tag: this.$route.query.searchtag,
	  }
  },
  methods:{
	  tag_name(){
		  switch (this.search_tag) {
			  case "1":
				return "二手书本";
				break;
			  case "2":
				return "数码产品";
				break;
			  case "3":
				return "票务转让";
				break;
			  case "4":
				return "二手衣物";
				break;
			  case "5":
				return "生活用品";
				break;
			  case "6":
				return "运动装备";
				break;
			  default:
				return "其他二手";
		  }
	  }
  }
};
</script>

<style>
#tagpage {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  float:center;
  margin:auto;
}
#header {
	text-align: center;
	padding: unset;
}
.panel{
	/*width: 100%;*/
}
.el-main-panel{
	height: 100%;
	overflow-y: hidden;
}
</style>
