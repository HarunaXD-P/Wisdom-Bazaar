const {
    username
} = require('../src/page/login.vue')
describe('login',function(){
    let = Constructor = Vue.extend(login)
    const vm =new Constructor()
    expect(vm.username).to.equal("")
})