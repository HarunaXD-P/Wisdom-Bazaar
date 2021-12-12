// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui';
import App from './App'
import router from './router'
import initSqlJs from "sql.js"

//import './utils/flexible'
//import 'lib-flexible'
//import './utils/rem'

// Required to let webpack 4 know it needs to copy the wasm file to our assets
import sqlWasm from "!!url-loader?name=sql-wasm-[contenthash].wasm!sql.js/dist/sql-wasm.wasm";



Vue.use(ElementUI);

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
})

/*
async function loadDB() {
  try {
      const SQL = await initSqlJs({
          locateFile: () => sqlWasm
      });
      return new SQL.Database()
  } catch (err) {
      console.log(err);
  }
}
loadDB().then(db => app.config.globalProperties.$db = db) 
*/