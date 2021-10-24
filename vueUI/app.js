const routes=[
    {path:'/principal',component:principal},
    {path:'/administrativo',component:administrativo},
    {path:'/facultad',component:facultad}
]

const router=new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount('#app')