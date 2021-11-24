<template>
  <div>
    <div id="longbar">
        <div id="content">
          <div style="font-size:40px">{{product_name}}</div>
          <div>
            {{product_description}}
          </div>
        </div>
    </div>
  </div>
</template>

<script>

export default {
  data(){
    return{
      product_name:"加载中",
      product_description:"加载中"
    }
  },
  methods:{

  },
  created(){
    console.log(this.product_name);

  }

  
  

}
</script>

<style>
#longbar{
    width:1300px;
    height:150px;
    background-color:salmon;
    margin:auto;
    margin-bottom: 30px;
}
#content{
  width:700px;
  height:100px;
}

</style>