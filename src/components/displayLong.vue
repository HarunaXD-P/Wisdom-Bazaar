<template>
  <div>
    <div id="longbar">
        <div id="content">
          <div style="font-size:40px">{{local.name}}</div>
          <div>
            {{local.descript}}
          </div>
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

  },
  created(){
    console.log(this.product_name);

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
  width:700px;
  height:100px;
}

</style>