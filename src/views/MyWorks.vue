<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="7" class="el-menu-vertical-demo">
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
        <h2>我的作品</h2>
        <el-tabs v-model="activeTab">
          <el-tab-pane label="文本作品" name="text">
            <el-card v-for="work in textWorks" :key="work.id">
              <h3>{{ work.title }}</h3>
              <p>{{ work.content.slice(0, 100) }}...</p>
            </el-card>
          </el-tab-pane>
          <el-tab-pane label="图片作品" name="image">
            <el-row :gutter="20">
              <el-col :span="8" v-for="work in imageWorks" :key="work.id">
                <el-card>
                  <img :src="work.url" style="width:100%" />
                  <p>{{ work.title }}</p>
                </el-card>
              </el-col>
            </el-row>
          </el-tab-pane>
          <el-tab-pane label="视频作品" name="video">
            <el-card v-for="work in videoWorks" :key="work.id">
              <video :src="work.url" controls style="width:100%" />
              <p>{{ work.title }}</p>
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
const activeTab = ref('text')
const textWorks = ref([
  { id: 1, title: '我的第一篇文章', content: '这是我生成的第一篇文本内容...' },
  { id: 2, title: 'AI技术报告', content: '人工智能正在改变世界...' }
])
const imageWorks = ref([
  { id: 1, title: '风景图', url: 'https://picsum.photos/400/300?random=1' },
  { id: 2, title: '人物图', url: 'https://picsum.photos/400/300?random=2' }
])
const videoWorks = ref([])

function handleLogout() {
  API.logout()
  router.push('/')
}
</script>

<style scoped>
.dashboard { min-height: 100vh; }
.el-menu-vertical-demo { height: 100vh; }
</style>