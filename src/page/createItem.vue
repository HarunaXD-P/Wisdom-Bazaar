<!-- the page to create a commodity item -->
<template>
  <div id="app">
      <el-container class="panal">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header>
        <Header> </Header>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main>
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container>
          <goodsCreate></goodsCreate>
          <myInfirmation></myInfirmation>
        </el-container>
      </el-main>
    </el-container>

  </div>
</template>

<script>
import myHeader from "@/components/myHeader";
import goodsCreate from　"@/components/goodsCreate";
import GoodsCreate from '../components/goodsCreate.vue';
export default {
    name:"App",
  data () {
    return {
    };
  },

  components: {
      name: "App",
        components: {
            Header: myHeader,
            goodsCreate:goodsCreate,
            myInfirmation: information,
  }
  },

  computed: {},

  mounted: {},

  methods: {}
}

</script>
<style>
</style>