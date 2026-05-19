import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'Login', component: () => import('../views/Login.vue') },
  { path: '/register', name: 'Register', component: () => import('../views/Register.vue') },
  { path: '/dashboard', name: 'Dashboard', component: () => import('../views/Dashboard.vue') },
  { path: '/text', name: 'TextGenerate', component: () => import('../views/TextGenerate.vue') },
  { path: '/image', name: 'ImageGenerate', component: () => import('../views/ImageGenerate.vue') },
  { path: '/video', name: 'VideoGenerate', component: () => import('../views/VideoGenerate.vue') },
  { path: '/audio', name: 'AudioGenerate', component: () => import('../views/AudioGenerate.vue') },
  { path: '/tasks', name: 'Tasks', component: () => import('../views/Tasks.vue') },
  { path: '/works', name: 'MyWorks', component: () => import('../views/MyWorks.vue') },
  { path: '/resources', name: 'Resources', component: () => import('../views/Resources.vue') },
  { path: '/admin', name: 'Admin', component: () => import('../views/Admin.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router