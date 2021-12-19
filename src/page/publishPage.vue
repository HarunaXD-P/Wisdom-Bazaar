<!-- the page to create a commodity item -->
<template>
  <div name="createItem">
      <el-container class="panal">
      <!--header为上半部分，放了myHeader.vue中的组件-->
      <el-header style="padding: unset;">
        <myHeader> </myHeader>
      </el-header>
      <!--main为下半部分，放了LeftSidebar.vue和DisplaySix.vue和myInformation.vue中的三个组件-->
      <el-main style="padding: unset;">
        <!--加一个el-container是为了让这三个组件能左中右排布-->
        <el-container style="margin-left: 20px;">
          <myPublish></myPublish>
          <myInformation></myInformation>
        </el-container>
      </el-main>
    </el-container>

  </div>
</template>

<script>
import Header from "@/components/myHeader";
import goodsPublish from '@/components/goodsPublish.vue';
import information from '@/components/myInformation.vue';
import "element-ui/lib/theme-chalk/index.css";
export default {
    
  data () {
    
    return {
    };
  },

  name:"createItem",
  components: {
    myHeader: Header,
    myPublish:goodsPublish,
    myInformation: information,
  },
    

  computed: {},

  mounted: {},

  methods: {}
}

</script>
<style>

</style>