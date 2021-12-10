<template>
  <div id="app">
    <Header> </Header>
    <div id="cai_good_detail">
      <ul id="caimenu">
        <!-- 这四个超链接暂时先这样凑活一下，以后要改 -->
        <!-- 鼠标进入时会改变颜色 -->
        <li
          id="caimenu_sy"
          @mouseover="gd_changeBcolor($event, '#a2a19f')"
          @mouseleave="gd_changeBcolor($event, '#E8E7E3')"
        >
          <a href="http://www.baidu.com" title="首页"> 首页 </a>
        </li>
        <li
          id="caimenu_sc"
          @mouseover="gd_changeBcolor($event, '#a2a19f')"
          @mouseleave="gd_changeBcolor($event, '#E8E7E3')"
        >
          <a href="http://www.baidu.com" title="商城"> 商城 </a>
        </li>
        <li
          id="caimenu_qg"
          @mouseover="gd_changeBcolor($event, '#a2a19f')"
          @mouseleave="gd_changeBcolor($event, '#E8E7E3')"
        >
          <a href="http://www.baidu.com" title="求购"> 求购 </a>
        </li>
        <li
          id="caimenu_lxwm"
          @mouseover="gd_changeBcolor($event, '#a2a19f')"
          @mouseleave="gd_changeBcolor($event, '#E8E7E3')"
        >
          <a href="http://www.baidu.com" title="联系我们"> 联系我们</a>
        </li>
      </ul>
    </div>

    <div id="cai_detail_box">
      <div style="height: 640px">
        <!-- 这里放商品详情框上面的部分 -->
        <div style="width: 0px; height: 0px">
          {{ getDetail() }}
        </div>
        <div style="width: 684px; height: 464px; float: left">
          <!-- 这里放图片 -->
          <img
            src="../assets/iphone.jpeg"
            width="684px"
            height="464px"
          /><img />
        </div>
        <div
          style="
            width: 386px;
            height: 71px;
            margin-left: 64px;
            font-size: 48px;
            float: left;
          "
        >
          {{ title }}
        </div>
        <div
          style="
            width: 299px;
            height: 30px;
            margin-left: 66px;
            font-size: 20px;
            color: red;
            float: left;
          "
        >
          {{ description }}
        </div>
        <div
          style="
            width: 412px;
            height: 71px;
            margin-left: 64px;
            font-size: 48px;
            float: left;
          "
        >
          <p style="margin: 0px; padding: 0px; color: gray; float: left">
            价格
          </p>
          <p style="margin: 0px; padding: 0px; color: red; float: right">
            ￥{{ price }}
          </p>
        </div>

        <!-- 画一条横线 -->
        <div style="height: 10px; width: 499px; margin-left: 42px; float: left">
          <hr />
        </div>
        <div
          style="
            width: 216px;
            height: 106px;
            margin-left: 41px;
            margin-top: 59px;
            float: left;
            font-size: 36px;
            color: rgba(181, 161, 161, 1);
          "
        >
          方便交易时间<br />
          全天
        </div>
        <!-- 画一条竖线 -->
        <div
          style="
            width: 10px;
            height: 176px;
            margin-left: 35px;
            margin-top: 24px;
            float: left;
            border-left: 1px solid rgba(166, 166, 166, 1);
          "
        ></div>
        <div
          style="
            width: 216px;
            height: 106px;
            margin-left: 25px;
            margin-top: 59px;
            float: left;
            font-size: 36px;
            color: rgba(181, 161, 161, 1);
          "
        >
          剩余有效期<br />
          30天
        </div>
        <!-- 画一条横线 -->
        <div
          style="
            height: 10px;
            width: 499px;
            margin-left: 42px;
            margin-top: 31px;
            float: left;
          "
        >
          <hr />
        </div>

        <!-- 下面还有两个按钮 -->
        <div
          style="
            height: 130px;
            width: 535px;
            margin-left: 42px;
            margin-top: 42px;
            float: left;
          "
        >
          <button
            type="button"
            style="
              height: 130px;
              width: 240px;
              float: left;
              font-size: 48px;
              background-color: rgba(255, 77, 79, 1);
              border-radius: 15px;
              color: white;
            "
            @click="dialog_buying_Visible=true"
          >
            立即联系
          </button>
          <button
            type="button"
            style="
              height: 130px;
              width: 240px;
              margin-left: 20px;
              float: left;
              font-size: 48px;
              background-color: rgba(232, 169, 132, 1);
              border-radius: 15px;
              color: white;
            "
          >
            加购物车
          </button>
        </div>
      </div>

      <div>
        <!-- 这里放 商品详情 文字部分 -->
        <!-- 字体什么的，以后再管了 -->
        <div
          style="
            height: 119px;
            width: 100%;
            float: left;
            background-color: rgba(196, 196, 196, 1);
          "
        >
          <p
            style="
              margin: 0px 0px 0px 35px;
              padding: 0px;
              color: white;
              float: left;
              font-size: 48px;
              line-height: 119px;
            "
          >
            商品详情
          </p>
        </div>
        <div style="min-height: 118px; width: 100%; float: left">
          <p
            style="
              margin: 10px 0px 0px 41px;
              padding: 0px;
              float: left;
              font-size: 36px;
              text-align: left;
              color: rgba(120, 66, 66, 1);
            "
          >
            据介绍，iPhone13Pro正面采用一块6.1英寸的OLED屏，屏幕刷新率120Hz，支持1Hz至120Hz刷新率调节，
            屏幕分辨率2532X1170，机身厚度7.65mm，重203g。
            拍照上，Pro版本后置采用三颗1200万像素的镜头，
            1200万像素广角，1200万像素超广角，和1200万像素长焦，支持3倍光学变焦，15倍数码变焦。
            广角镜头和长焦镜头都支持光学防抖。
          </p>
        </div>
        

          <el-dialog
            :visible.sync="dialog_buying_Visible"
            width="50%"
            style="text-align: center"
            :before-close="handleClose"
          >
            <!-- <repassword></repassword> -->
            <span>确认购买</span>
            <el-input v-model="checkbuy"></el-input>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialog_buying_Visible = false">取 消</el-button>
              <el-button type="primary" @click="buyProduct"
                >确 定</el-button
              >
            </span>
          </el-dialog>
        
      </div>
    </div>
    <div style="float: right">
      <myInfirmation> </myInfirmation>
    </div>
  </div>
</template>

<script>
import myHeader from "@/components/myHeader";
import LeftSidebar from "@/components/LeftSidebar";
import DisplaySix from "@/components/DisplaySix";
import information from "@/components/myInformation";
import "element-ui/lib/theme-chalk/index.css";
import _first from "@/components/cai_msg";
import axios from "axios";
import GLOBAL from '@/global/global'

export default {
  name: "App",
  data() {
    return {
      title: "",
      description: "",
      price: 0,
      value: "",
      product_id: "",
      dialog_buying_Visible: false,
      checkbuy:""
    };
  },
  components: {
    Header: myHeader,
    myLeftSidebar: LeftSidebar,
    myDisplay: DisplaySix,
    myInfirmation: information,
    dongtai: _first,
  },
  methods: {
    gd_changeBcolor(x, color) {
      x.currentTarget.style.background = color;
    },
    getDetail() {
      console.log("!!!!!!1");
      //在这里传给后端
      var that = this;
      const path = "http://127.0.0.1:5000/productinfo"; // 我也不知道
      var goodsInformation = {
        product_id: 1,
      };
      axios
        .post(path, JSON.stringify(goodsInformation))
        .then(function (response) {
          // response.setContentType("text/javascript;charset=UTF-8");
          var goods = response.data;
          console.log("!!!!!!!!!!!!!!!!" + goods["product_name"]);
          console.log(goods["description"]);
          console.log(goods["price"]);
          console.log(goods["number"]);
          console.log(goods["value"]);
          // modified by xcc 2021.11.24 21:57
          that.title = goods["product_name"];
          that.description = goods["description"];
          that.price = goods["price"];
          that.value = goods["category_value"];
        });
    },
    handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
    handleConfirm(){
      console.log(this.checkbuy);
      this.dialog_buying_Visible=false;
    },
    buyProduct() {
      //如果没有登陆的话.....currentUser_id究竟是undefined还是空串呢
      if(GLOBAL.currentUser_ID=="")
      {
        alert("目前尚未登陆，请登录后再进行操作!");
      }
      //获取当前的时间，命名可谓是非常简陋
      let yy = new Date().getFullYear();
      let mm = new Date().getMonth() + 1;
      let dd = new Date().getDate();
      let hh = new Date().getHours();
      let mf =
        new Date().getMinutes() < 10
          ? "0" + new Date().getMinutes()
          : new Date().getMinutes();
      var nowTime=hh+":"+mf;
      var nowDate=yy+"-"+mm+"-"+dd;

      //获取商品和买家信息
      const  path="http://39.104.84.38:8080/buyproduct";
      var buyEvent={
        "buyer_id":GLOBAL.currentUser_ID,
        "sold_product_id":this.product_id,
        "time":nowDate + ' ' + nowTime,
      }

      //此处打印很成功，注意键值对的格式
      console.log(buyEvent);

      axios
					.post(path,JSON.stringify(buyEvent))
					.then(function(response){
						var buy_result=response.data
						is_buy_success = login_result["result"];
						//alart(is_register_success)
						console.log(is_register_success);//注意返回格式
						if(is_buy_success==="failed"){
							alert("购买失败，请重试");
						}else if(is_register_success==="success"){
              var alert_str="购买成功，卖家的微信为:"+buy_result["seller_wechat"]+" 请及时联系"
							alert(alert_str);
              this.dialog_buying_Visible=false;
						}else{
							alert("买了个什么玩意？");
						}
					});
    },
  },
  props: ["goodId"],
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-right: 0px;
  width: 1920px;
  height: 1080px;
  float: center;
  margin: auto;
}

#cai_good_detail {
  height: 48px;
  width: 1120px;
  padding-top: 0px;
  margin-left: 400px;
  border: 0px;
  background: #e8e7e3;
}

#caimenu {
  padding: 0px;
  position: relative;
  text-align: center;
}

#caimenu_sy {
  height: 48px;
  width: 280px;
  list-style: none;
  float: left;
  font-size: 30px;
}

#caimenu_sc {
  height: 48px;
  width: 280px;
  list-style: none;
  float: left;
  font-size: 30px;
}

#caimenu_qg {
  height: 48px;
  width: 280px;
  list-style: none;
  float: left;
  font-size: 30px;
}

#caimenu_lxwm {
  height: 48px;
  width: 280px;
  list-style: none;
  float: left;
  font-size: 30px;
}

#cai_detail_box {
  width: 1261px;
  mim-height: 880px;
  margin-left: 256px;
  margin-top: 30px;
  float: left;
}
#demo {
  width: 100px;
  height: 100px;
  background-color: blue;
}
</style>
