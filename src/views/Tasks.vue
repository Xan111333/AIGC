<template>
  <div class="dashboard">
    <el-container>
      <el-aside width="200px">
        <el-menu default-active="6" class="el-menu-vertical-demo">
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
        <h2>任务管理</h2>
        <el-button type="primary" @click="showAdd = true">新建任务</el-button>
        <el-table :data="tasks" style="width:100%">
          <el-table-column prop="title" label="任务名称" />
          <el-table-column prop="description" label="描述" />
          <el-table-column prop="status" label="状态" />
          <el-table-column prop="deadline" label="截止日期" />
          <el-table-column label="操作">
            <template #default="scope">
              <el-button @click="editTask(scope.row)">编辑</el-button>
              <el-button @click="deleteTask(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-dialog v-model="showAdd" title="新建任务">
          <el-form :model="taskForm">
            <el-form-item label="任务名称">
              <el-input v-model="taskForm.title" />
            </el-form-item>
            <el-form-item label="描述">
              <el-textarea v-model="taskForm.description" />
            </el-form-item>
            <el-form-item label="截止日期">
              <el-date-picker v-model="taskForm.deadline" />
            </el-form-item>
          </el-form>
          <template #footer>
            <el-button @click="showAdd = false">取消</el-button>
            <el-button type="primary" @click="addTask">确定</el-button>
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
const tasks = ref([
  { id: 1, title: '学习文本生成', description: '完成文本生成模块学习', status: '进行中', deadline: '2024-01-20' },
  { id: 2, title: '图片生成练习', description: '完成图片生成练习', status: '未开始', deadline: '2024-01-25' }
])
const showAdd = ref(false)
const taskForm = ref({ title: '', description: '', deadline: '' })

async function addTask() {
  try {
    await API.post('/api/tasks', taskForm.value)
    showAdd.value = false
    taskForm.value = { title: '', description: '', deadline: '' }
    alert('任务创建成功')
  } catch (e) {
    alert('创建失败')
  }
}

function editTask(task) {
  alert('编辑任务: ' + task.title)
}

function deleteTask(id) {
  if (confirm('确定删除?')) {
    tasks.value = tasks.value.filter(t => t.id !== id)
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