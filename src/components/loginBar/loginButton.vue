<!-- 右上角的两个按钮，现在包装为一个组件，好在登陆完成时切换 -->
<template>
  <div>
      <span id="loginButton">
        <!--这里加了一个跳转到登陆的功能-->
        <el-button type="primary" @click="gotoLogin">登陆</el-button>
        <el-button type="primary" @click="gotoRegister">注册</el-button>
      </span>
  </div>
</template>

<script>
export default {
  data () {
    return {
    };
  },

  components: {},

  computed: {},

  mounted: {},

  methods: {
    gotoLogin()
    {
      this.$router.replace('/login')
      //this.$router.go(0)
    },
	  gotoRegister()
    {
      this.$router.replace('/register')
      //this.$router.go(0)
    }
  }
}

</script>

<style>
#loginButton {
  float: right;
}
</style>