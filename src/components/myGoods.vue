<template>
  <div>
      <ul>
          <li v-for="(item,index) in myGoodsData" :key="index">
                <display-long :oneItemData="myGoodsData[index]" :oneItemType="type"></display-long>
                
          </li>
      </ul>
  </div>
</template>

<script>
import Display from './Display.vue'
import displayLong from './displayLong.vue'
export default {
    components:{displayLong},
    props:['myGoodsData','type'],
    data(){
        
        return{
            goodsnum:3,
            
            //displayLongData:[{'name':"FC31",'descript':"haisidai"},{'name':"FC31",'descript':"wudaiji"},{'name':"F22","descript":'niangniang'}],
            
        }
    },
    created(){
    

    },
    updated(){
        console.log(this.myGoodsData);
        
    },
    methods:{

    },

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