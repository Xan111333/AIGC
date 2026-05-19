<template>
  <div class="register-container">
    <el-card class="register-card">
      <h2>注册账号</h2>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="form.email" placeholder="请输入邮箱" />
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="form.role" placeholder="请选择角色">
            <el-option label="学生" value="student" />
            <el-option label="教师" value="teacher" />
            <el-option label="管理员" value="admin" />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleRegister" style="width:100%">注册</el-button>
        </el-form-item>
        <el-form-item>
          <el-button @click="goLogin" style="width:100%">返回登录</el-button>
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
const form = ref({ username: '', password: '', email: '', role: 'student' })

async function handleRegister() {
  try {
    const res = await API.post('/api/auth/register', form.value)
    if (res.id) {
      alert('注册成功')
      await router.push('/')
    }
  } catch (e) {
    alert('注册失败')
  }
}

function goLogin() {
  router.push('/')
}
</script>

<style scoped>
.register-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.register-card {
  width: 400px;
  padding: 30px;
  text-align: center;
}
h2 {
  margin-bottom: 30px;
  color: #333;
}
</style>