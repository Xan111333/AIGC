<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>AIGC实训平台</h2>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin" style="width:100%">登录</el-button>
        </el-form-item>
        <el-form-item>
          <el-button @click="goRegister" style="width:100%">注册新账号</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import API from '../api'

const router = useRouter()
const form = ref({ username: '', password: '' })

async function handleLogin() {
  try {
    const res = await API.login(form.value.username, form.value.password)
    if (res.access_token) {
      await router.push('/dashboard')
    }
  } catch (e) {
    alert('登录失败')
  }
}

function goRegister() {
  router.push('/register')
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.login-card {
  width: 400px;
  padding: 30px;
  text-align: center;
}
h2 {
  margin-bottom: 30px;
  color: #333;
}
</style>