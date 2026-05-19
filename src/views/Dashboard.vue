<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="1" class="el-menu-vertical-demo">
          <el-menu-item index="1" @click="$router.push('/dashboard')">首页</el-menu-item>
          <el-menu-item index="2" @click="$router.push('/text')">文本生成</el-menu-item>
          <el-menu-item index="3" @click="$router.push('/image')">图片生成</el-menu-item>
          <el-menu-item index="4" @click="$router.push('/video')">视频生成</el-menu-item>
          <el-menu-item index="5" @click="$router.push('/audio')">音频生成</el-menu-item>
          <el-menu-item index="6" @click="$router.push('/tasks')">任务管理</el-menu-item>
          <el-menu-item index="7" @click="$router.push('/works')">我的作品</el-menu-item>
          <el-menu-item index="8" @click="$router.push('/resources')">学习资源</el-menu-item>
          <el-menu-item index="9" @click="$router.push('/admin')">管理后台</el-menu-item>
          <el-menu-item index="10" @click="handleLogout">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <h2>欢迎来到 AIGC 实训平台</h2>
        <el-row :gutter="20">
          <el-col :span="6"><el-card>文本生成</el-card></el-col>
          <el-col :span="6"><el-card>图片生成</el-card></el-col>
          <el-col :span="6"><el-card>视频生成</el-card></el-col>
          <el-col :span="6"><el-card>音频生成</el-card></el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import API from '../api'

const router = useRouter()

function handleLogout() {
  API.logout()
  router.push('/')
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
}
.el-menu-vertical-demo {
  height: 100vh;
}
</style>