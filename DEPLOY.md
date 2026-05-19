# AIGC 实训平台 - 部署指南

## 快速部署

### 1. 上传代码到 GitHub
- 解压压缩包
- 上传到 GitHub 仓库

### 2. 部署后端到 Vercel
- 打开 https://vercel.com
- 导入 GitHub 仓库
- 设置 Root Directory 为 `backend`
- 点击 Deploy
- 获取域名（如 https://xxx.vercel.app）

### 3. 配置前端
- 在 GitHub 创建 `.env.production` 文件：
  ```
  VITE_API_URL=https://xxx.vercel.app
  ```

### 4. 开启 GitHub Pages
- 在仓库设置中找到 Pages
- 选择 main 分支
- 保存

## 启动命令

```bash
npm install && npm run dev
cd backend && pip install -r requirements.txt && python main.py
```

## 功能模块

- ✅ 用户登录/注册
- ✅ 文本生成
- ✅ 图片生成
- ✅ 视频生成
- ✅ 音频生成
- ✅ 任务管理
- ✅ 我的作品
- ✅ 学习资源
- ✅ 管理后台