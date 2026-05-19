<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="4" class="el-menu-vertical-demo">
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
        <h2>视频生成</h2>
        <el-form :model="form">
          <el-form-item label="输入提示">
            <el-textarea v-model="form.prompt" rows="4" placeholder="请输入视频生成提示" />
          </el-form-item>
          <el-form-item label="时长(秒)">
            <el-select v-model="form.duration">
              <el-option label="5秒" :value="5" />
              <el-option label="10秒" :value="10" />
              <el-option label="15秒" :value="15" />
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="generate">生成</el-button>
          </el-form-item>
        </el-form>
        <el-card v-if="result">
          <h3>生成结果</h3>
          <video :src="result" controls style="max-width:100%" />
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import API from '../api'

const router = useRouter()
const form = ref({ prompt: '', duration: 5 })
const result = ref('')

async function generate() {
  try {
    const res = await API.post('/api/video/generate', form.value)
    result.value = res.url || ''
  } catch (e) {
    result.value = ''
    alert('生成失败')
  }
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