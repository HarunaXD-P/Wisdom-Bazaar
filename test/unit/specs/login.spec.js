import Vue from 'vue'
import login from '@/page/login.vue'

describe('login.vue',()=>{
    it('should render correct contents',()=>{
        const Constructor = Vue.extend(login)
        const vm = new Constructor().$mount()
        expect(vm.form.username)
        .toEqual("")
    })
})