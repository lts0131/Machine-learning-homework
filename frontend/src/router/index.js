import Vue from 'vue'
import Router from 'vue-router'
import login from '@/pages/login'
import index from '@/pages/index'

Vue.use(Router)

export default new Router({
    routes: [{
        path: '/',
        name: 'index',
        component: login
    }, {
        path: '/index',
        name: 'index',
        component: index
    }]
})
