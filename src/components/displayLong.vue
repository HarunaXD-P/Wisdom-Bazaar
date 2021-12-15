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
          <div id="blank">   </div>
          <div @click="dialog_delete_Visible=true">删除商品</div>

        </div>
    </div>
    <el-dialog
            :visible.sync="dialog_delete_Visible"
            width="50%"
            style="text-align: center"
            :before-close="handleClose"
          >
            <!-- <repassword></repassword> -->
            <span>确认删除{{this.local.product_name}}吗</span>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialog_delete_Visible = false">取 消</el-button>
              <el-button type="primary" @click="deleteProduct"
                >确 定</el-button
              >
            </span>
          </el-dialog>
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
      dialog_delete_Visible: false,
    }
  },
  methods:{
    showDetails(){
      var a=this.local.product_id;
      this.$router.push({path:'/goodDetail',query:{product_id:a}});
    },
    deleteProduct(){
      const path="http://39.104.84.38:8080/deleteproduct";
      var deleteinfo={
        "deleteproduct_id":this.local.product_id,
      };
      axios
					.post(path,JSON.stringify(deleteinfo))
					.then(function(response){
						var delete_result=response.data
						var  is_delete_success = delete_result["result"];
						//alart(is_register_success)
						console.log(delete_result);//注意返回格式
						if(is_delete_success==="failed"){
							alert("删除失败，请重试");
              that.dialog_buying_Visible=false;
						}else if(is_buy_success==="success"){
              var alert_str="删除成功"
							alert(alert_str);
              that.dialog_buying_Visible=false;
						}else{
							alert("删除了个什么玩意？");
						}
					});

    },
    handleClose(done) {
        this.$confirm('确认取消？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

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
#blank{
  height:10px;
}

</style>