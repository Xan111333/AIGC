<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="9" class="el-menu-vertical-demo">
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
        <h2>管理后台</h2>
        <el-tabs v-model="activeTab">
          <el-tab-pane label="用户管理" name="users">
            <el-button type="primary" @click="showAddUser = true">添加用户</el-button>
            <el-table :data="users" style="width:100%">
              <el-table-column prop="username" label="用户名" />
              <el-table-column prop="email" label="邮箱" />
              <el-table-column prop="role" label="角色" />
              <el-table-column label="操作">
                <template #default="scope">
                  <el-button @click="editUser(scope.row)">编辑</el-button>
                  <el-button @click="deleteUser(scope.row.id)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane label="系统配置" name="config">
            <el-form :model="config">
              <el-form-item label="网站名称">
                <el-input v-model="config.siteName" />
              </el-form-item>
              <el-form-item label="最大生成次数">
                <el-input v-model="config.maxGenerations" />
              </el-form-item>
              <el-button type="primary" @click="saveConfig">保存配置</el-button>
            </el-form>
          </el-tab-pane>
        </el-tabs>
        <el-dialog v-model="showAddUser" title="添加用户">
          <el-form :model="userForm">
            <el-form-item label="用户名">
              <el-input v-model="userForm.username" />
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="userForm.password" type="password" />
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="userForm.email" />
            </el-form-item>
            <el-form-item label="角色">
              <el-select v-model="userForm.role">
                <el-option label="学生" value="student" />
                <el-option label="教师" value="teacher" />
                <el-option label="管理员" value="admin" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
            <el-button @click="showAddUser = false">取消</el-button>
            <el-button type="primary" @click="addUser">确定</el-button>
          </template>
        </el-dialog>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import API from '../api'

const router = useRouter()
const activeTab = ref('users')
const users = ref([
  { id: 1, username: 'admin', email: 'admin@example.com', role: 'admin' },
  { id: 2, username: 'teacher1', email: 'teacher@example.com', role: 'teacher' },
  { id: 3, username: 'student1', email: 'student@example.com', role: 'student' }
])
const showAddUser = ref(false)
const userForm = ref({ username: '', password: '', email: '', role: 'student' })
const config = ref({ siteName: 'AIGC实训平台', maxGenerations: 100 })

async function addUser() {
  try {
    await API.post('/api/admin/users', userForm.value)
    showAddUser.value = false
    userForm.value = { username: '', password: '', email: '', role: 'student' }
    alert('用户添加成功')
  } catch (e) {
    alert('添加失败')
  }
}

function editUser(user) {
  alert('编辑用户: ' + user.username)
}

function deleteUser(id) {
  if (confirm('确定删除?')) {
    users.value = users.value.filter(u => u.id !== id)
  }
}

function saveConfig() {
  alert('配置保存成功')
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