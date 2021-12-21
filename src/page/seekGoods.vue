<!--
<template>
  <div class="DisplaySix">
  -->
    <!--这个整体为一个面板，这个面板分为header和main两个面板，这两个每个再分别由3个Display.vue中的类构成-->
    <!--总体效果就是将Display.vue中的效果复制为6份，布局为每行3个，每列两个-->
    <!--
    <el-container class="PanelWhole">
      <el-header height="400px">
        <el-container>
          <myDisplay class="PanelPart"></myDisplay>
          <myDisplay class="PanelPart"></myDisplay>
          <myDisplay class="PanelPart"></myDisplay>
        </el-container>
      </el-header>
      <el-main height="400px">
        <el-container>
          <myDisplay class="PanelPart"></myDisplay>
          <myDisplay class="PanelPart"></myDisplay>
          <myDisplay class="PanelPart"></myDisplay>
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>
-->
<template>
  <div class="seekGoods" id="newApp">
    <el-container class="panel">
      <el-header style="padding: unset">
        <myHeader> </myHeader>
      </el-header>
      <el-main style="padding: unset;">
        <el-container class="el-main-panel">
          <myLeftSidebar></myLeftSidebar>
          <div>
          <seekDisplay
            v-for="(item, index) in goods"
            :key="index"
            style="float: left; margin: 10px"
            :goodsContent="goods[index]"
          ></seekDisplay>
          </div>
          <myInformation></myInformation>
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import DisplaySeek from "@/components/DisplaySeek";
import LeftSidebar from "@/components/LeftSidebar";
import axios from "axios";
import "element-ui/lib/theme-chalk/index.css";
import information from "@/components/myInformation.vue";
import Header from "@/components/myHeader";
export default {
  name: "seekGoods",
  data() {
    return {
      goods: [],
    };
  },
  components: {
    myHeader: Header,
    myLeftSidebar: LeftSidebar,
    seekDisplay: DisplaySeek,
    myInformation: information,
  },
  created: function () {
    this.initialize();
    this.title = "myTry";
  },
  methods: {
    initialize() {
      this.description = "not a book";
      const that = this;
      const path = "http://39.104.84.38:8080/userallwanted";
      var getGoods = {
        strategy_0: 0,
        strategy_1: 0,
        source_id: 0,
        category_value: 0,
      };
      axios.post(path, JSON.stringify(getGoods)).then(function (response) {
        that.goods = response.data;
        console.log(that.goods);
      });
      /*
     this.goods=[{product_name:"嘉然小姐",description:"急需一只嘉然小姐，价格面议，嘉然，你带我走吧",price:"20"},
     {product_name:"亭亭April",description:"重金征求信科xjj教我学编译"},
     {product_name:"陈睿",description:"重金悬赏叔叔"}]
     */
    },
    debug() {
      console("I'm here");
    },
  },
};
</script>

<style>
/*设置整个面板的长和宽 */

.seekGoods {
  background-color: #ffffff;
}
#newApp {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/

  float: center;
  margin: auto;
  background-color: #ffffff;
}
#header {
  /*line-height: 60px;*/
  /*background-color: #3896C2;*/
  text-align: center;
  padding: unset;
}
.panel {
  /*width: 100%;*/
}
.el-main-panel {
  height: 100%;
  overflow-y: hidden;
}
</style>