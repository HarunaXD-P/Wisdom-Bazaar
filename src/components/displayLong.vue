<template>
  <div v-if="display_total">
    <div id="longbar">
        <div id=img>
          <img :src=local.photo id="photo">
        </div>
        <div id="content">
          <div style="font-size:40px">{{local.product_name}}</div>
          <div>商品ID：{{local.product_id}}</div>
          <div>
           商品描述： {{local.description}}
          </div>
        </div>
        <div id="price_num">
          <div style="font-size:30px; width:300px">价格：{{local.price}}</div>
          <div v-if="display_time">购买时间：{{local.time}}</div>
          <div v-if="display_wechat">卖家微信:{{local.seller_wechat}}</div>
        </div>
        <div id="operation">
          <div @click="showDetails" v-show="display_detail">查看商品信息</div>
          <div id="blank">   </div>
          <div @click="dialog_delete_Visible=true" v-if="display_delete">删除商品</div>

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
              <el-button type="primary" @click="doDelete"
                >确 定</el-button
              >
            </span>
          </el-dialog>
  </div>
</template>

<script>
import GLOBAL from "@/global/global";
import axios from "axios";
export default {
  props:['oneItemData','oneItemType'],
  data(){
    return{
      //product_name:oneItemData.name,
      //product_description:this.oneItemData.descript,
      local:this.oneItemData,
      dialog_delete_Visible: false,
      getType:this.oneItemType,
      display_delete:true,
      display_detail:true,
      display_time:true,
      display_wechat:false,
      display_total:true,
    }
  },
  watch:{

  },
  methods:{
    showDetails(){
      var a=this.local.product_id;
      var b=this.getType;
      this.$router.push({path:'/goodDetail',query:{product_id:a,type:b}});
    },
    debug(){
      console.log(this.getType);
      console.log("from displaylong");
    },
    selecttoHide(){
      if(this.getType=="mypurchase"){
        this.display_delete=false;
        this.display_wechat=true;

      }else if(this.getType=="userallproducts"){
        this.display_time=false;
      }
      else if(this.getType=="myfavorites"){
        this.display_time=false;


      }

    },
    deleteProduct(){
      console.log("enter deleteProduct");
      const path="http://39.104.84.38:8080/deleteproduct";
      var deleteinfo={
        "deleteproduct_id":this.local.product_id,
      };
      var that=this;
      axios
					.post(path,JSON.stringify(deleteinfo))
					.then(function(response){
						var delete_result=response.data;
						var is_delete_success = delete_result["result"];
						//alart(is_register_success)
						console.log(delete_result);//注意返回格式
            console.log(is_delete_success);
						if(is_delete_success=="failed"){
							alert("删除失败，请重试");
              that.dialog_buying_Visible=false;
						}else if(is_delete_success=="success"){
              var alert_str="删除成功"
              that.display_total=false;
              that.dialog_delete_Visible=false;
							alert(alert_str);
						}else{
							alert("删除了个什么玩意？");
						}
					});

    },
    deleteFromFavorite(){
      console.log("enter delete favorite")
      const path="http://39.104.84.38:8080/deletefavorites";
      var deleteinfo={
        "delete_id":this.local.product_id,
        "source_id":GLOBAL.currentUser_ID,
      };
      var that=this;
      axios
					.post(path,JSON.stringify(deleteinfo))
					.then(function(response){
						var delete_result=response.data
						var  is_delete_success = delete_result["result"];
						//alart(is_register_success)
						console.log(delete_result);//注意返回格式
						if(is_delete_success==="failed"){
							alert("删除失败，请重试");
              that.dialog_delete_Visible=false;
						}else if(is_delete_success==="success"){
              var alert_str="删除成功"
              that.display_total=false;
              that.dialog_delete_Visible=false;
							alert(alert_str);
              
						}else{
							alert("删除了个什么玩意？");
						}
					});

    },
    doDelete(){
      if(this.getType=="userallproducts"){
        console.log("选择了删除商品");
        this.deleteProduct();

      }
      else if(this.getType=="myfavorites"){
        console.log("选择了删除收藏");
        this.deleteFromFavorite();
      }
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
    this.selecttoHide();

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
  width:400px;
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
#photo{
  width:150px;
  height: 150px;
}
#price_num{
  width:300px;
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