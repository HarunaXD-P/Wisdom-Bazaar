<template>
  <div>
      wos zhanweifu n
      <ul>
          <li v-for="(item,index) in myGoodsData" :key="index">
                <div id="longbar">
                    <div id="content">
                        <div style="font-size:40px">{{item.name}}</div>
                        <div>
                            {{item.descript}}
                        </div>
                    </div>
                </div>
                
          </li>
      </ul>
  </div>
</template>

<script>
import displayLong from './displayLong.vue'
export default {
    components:{displayLong},
    data(){
        return{
            goodsnum:3,
            //displayLongData:[{'name':"FC31",'descript':"haisidai"},{'name':"FC31",'descript':"wudaiji"},{'name':"F22","descript":'niangniang'}],

        }
    },
    created(){
        console.log("initil");
        console.log(this.myGoodsData);
        console.log(this.myGoodsData[1]);

    },
    methods:{

    },
    props:['myGoodsData']

}
</script>

<style>
ul{
    list-style: none;
}
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