<template>
  <div class="DisplaySix">
    <!--这个整体为一个面板，这个面板分为header和main两个面板，这两个每个再分别由3个Display.vue中的类构成-->
    <!--总体效果就是将Display.vue中的效果复制为6份，布局为每行3个，每列两个-->

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

<script>
import Display from "@/components/Display";
import "element-ui/lib/theme-chalk/index.css";
export default {
  name: "App",
  components: {
    myDisplay: Display,
  },
};
</script>

<style>
/*设置整个面板的长和宽 */
.PanelWhole {
  width: 1000px;
  height: 1000px;
  margin-top: -70px;
  
  
}
/*设置6个部分之间的间隔 */
.PanelPart {
  margin: 50px;
}
</style>