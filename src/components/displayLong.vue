<template>
  <div>
    <div id="longbar">
        <div id=img>
        </div>
        <div id="content">
          <div style="font-size:40px">{{local.product_name}}</div>
          <div>商品ID：{{local.product_id}}</div>
          <div>
           商品描述： {{local.description}}
          </div>
        </div>
        <div id="price_num">
          <div style="font-size:30px">价格：{{local.price}}</div>
        </div>
        <div id="operation">
          <div @click="showDetails">查看商品信息</div>
          <div>   </div>
          <div>删除商品</div>

        </div>
    </div>
  </div>
</template>

<script>

export default {
  props:['oneItemData'],
  data(){
    return{
      //product_name:oneItemData.name,
      //product_description:this.oneItemData.descript,
      local:this.oneItemData,
    }
  },
  methods:{
    showDetails(){
      var a=this.local.product_id;
      this.$router.push({path:'/goodDetail',query:{product_id:a}});
    }

  },
  created(){
    //console.log(this.product_name);

  },
  
  

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
  width:500px;
  height:100px;
  display: inline-block;
  float: left;
  text-align: left;
  margin-left:70px;
}
#img{
  width:150px;
  height:150px;
  background-color: brown;
  display: inline-block;
  float: left;
}
#price_num{
  width:200px;
  height:100px;
  float:left;
  text-align: left;
  margin-left: 70px;
  margin-top:50px;
}
#operation{
  width:200px;
  height:100px;
  float:right;
  margin:auto;
  margin-top:50px;
}

</style>