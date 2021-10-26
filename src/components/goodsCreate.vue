<!-- upload a good with title,description,num and otc -->
<template>
  <div class="createInput">
      <div class="title">
          <span id="title">商品标题</span>
          <span id="inputTitle">
          <div id="titleTextbox">
              <el-input v-model="inputTitle" placeholder="请输入内容"></el-input>
              </div>
          </span>
      </div>
      
      <div class="description">
          <span id="description">商品描述</span>
          <span id="inputDescription">
          <div id="descriptionTextbox">
              <el-input v-model="inputDescription" 
                        type="textarea" 
                        placeholder="请输入内容" :autosize="{minRows:2,maxRows:5}"></el-input>
              </div>
          </span>
      </div>
      <div class="goodsNum">
          <span id="goodsNum">选择数量</span>
          <span id="selectNum">
              <el-input-number v-model="num" 
                                @change="handleChange" 
                                :min="1" :max="10" 
                                label="描述文字"></el-input-number>
              
          </span>
      </div>
      <div class="price">
          <span id="price">选择价格</span>
          <span id="inputPrice">
              <div id="priceTextbox">
              <el-input v-model="inputPrice" 
                        placeholder="请输入价格"
                        prefix-icon=""></el-input>
              </div>
              
          </span>
      </div>
      <div class="catagory">
          <span id="catagory">选择分类</span>
          <span id="selectCatagory">
              <div id="catagorySelector">
                   <el-select v-model="value" placeholder="请选择">
                     <el-option
                         v-for="item in options"
                         :key="item.value"
                        :label="item.label"
                        :value="item.value">
                     </el-option>
                    </el-select>
              </div>
              
          </span>
      </div>
      <div class="confirmButton">
          <div id="button">
              <el-button type="success">确认发布</el-button>

          </div>

      </div>
      
  </div>
</template>

<script>
export default {
  data () {
    return {
        inputTitle:'',
        inputDescription:'',
        inputPrice:'',
        num:1,
        options: [
            {value: '选项1',label: '二手书本'},
            {value: '选项2',label: '数码产品'}, 
            {value: '选项3',label: '票务转让'}, 
            {value: '选项4',label: '二手衣物'}, 
            {value: '选项5',label: '生活用品'},
            {value: '选项6',label: '运动装备'},
            {value: '选项7',label: '其他二手'}
            ],
        value: ''

    };
  },

  components: {},

  computed: {},

  mounted: {},

  methods: {
      handleChange(value) {
        console.log(value);
      }
  }
}

</script>

<style>
.createInput{
    float:right;
    position: relative;
    width:1405px;
    height:670px;
    background: chocolate;

    margin-top: 15px;
    
    border-top-style: solid;
    border-top-color: darkgray;
    border-top-width: 2px;
}
#titleTextbox,#descriptionTextbox{
    margin-left: 50px;
    width:400px;
}
#selectNum,#priceTextbox,#catagorySelector{
    margin-left: 50px;
}

.title{
    height:100px;
    width:670px;
    position: absolute;
    top:50px;
    left:50px;
}
.description{
    height:100px;
    width:670px;
    position: absolute;
    top:150px;
    left:50px;

}
.goodsNum{
    height:100px;
    width:670px;
    position: absolute;
    top:250px;
    left:50px;
}
.price{
    height:100px;
    width:670px;
    position: absolute;
    top:350px;
    left:50px;
}
.catagory{
    height:100px;
    width:670px;
    position: absolute;
    top:450px;
    left:50px;
}
.confirmButton{
    height:100px;
    width:670px;
    position: absolute;
    top:550px;
    left:50px;
}

#title,#inputTitle{
    float:left;
    margin:auto;

}
#description,#inputDescription{
    float:left;
}
#goodsNum,#selectNum{
    float:left;
}
#price,#inputPrice{
    float:left;
}
#catagory,#selectCatagory{
    float:left;
}
#button{
    float: center;
}
</style>