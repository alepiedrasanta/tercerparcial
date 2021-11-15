import Vue from 'vue'
import VueRouter from 'vue-router'
import actualizar from '@/components/actualizar'
import crear from '@/components/crear'
import listar from '@/components/listar'
 
Vue.use(VueRouter)
 
const routes = [  
  {
    path: '/computadora/listar',
    name: 'Computadora',
    component: listar
  },
  {
    path: '/computadora/crear',
    name: 'Ingresar',
    component: crear
  },
  {
    path: '/computadora/actualizar/:id/:marca/:detalles/:precio',
    name: 'Actualizar',
    component: actualizar
  },
]
 
const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router
