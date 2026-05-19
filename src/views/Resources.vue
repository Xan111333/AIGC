<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="8" class="el-menu-vertical-demo">
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
        <h2>学习资源</h2>
        <el-tabs v-model="activeTab">
          <el-tab-pane label="文档教程" name="docs">
            <el-card v-for="doc in docs" :key="doc.id">
              <h3>{{ doc.title }}</h3>
              <p>{{ doc.description }}</p>
              <el-button @click="openResource(doc)">查看</el-button>
            </el-card>
          </el-tab-pane>
          <el-tab-pane label="视频教程" name="videos">
            <el-card v-for="video in videos" :key="video.id">
              <video :src="video.url" controls style="width:100%" />
              <h3>{{ video.title }}</h3>
            </el-card>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import API from '../api'

const router = useRouter()
const activeTab = ref('docs')
const docs = ref([
  { id: 1, title: '文本生成入门', description: '学习如何使用文本生成功能' },
  { id: 2, title: '图片生成指南', description: '掌握图片生成技巧' },
  { id: 3, title: '视频生成教程', description: '学习视频生成方法' }
])
const videos = ref([])

function openResource(doc) {
  alert('打开资源: ' + doc.title)
}

function handleLogout() {
  API.logout()
  router.push('/')
}
</script>

<style scoped>
.dashboard { min-height: 100vh; }
.el-menu-vertical-demo { height: 100vh; }
</style>