const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const API = {
  async login(username, password) {
    const res = await fetch(`${BASE_URL}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    })
    const data = await res.json()
    if (data.access_token) localStorage.setItem('token', data.access_token)
    return data
  },

  async register(userData) {
    const res = await fetch(`${BASE_URL}/api/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    })
    return res.json()
  },

  async get(url, params = {}) {
    const token = localStorage.getItem('token')
    const query = new URLSearchParams(params).toString()
    const res = await fetch(`${BASE_URL}${url}${query ? '?' + query : ''}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {}
    })
    return res.json()
  },

  async post(url, data = {}) {
    const token = localStorage.getItem('token')
    const res = await fetch(`${BASE_URL}${url}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {})
      },
      body: JSON.stringify(data)
    })
    return res.json()
  },

  async put(url, data = {}) {
    const token = localStorage.getItem('token')
    const res = await fetch(`${BASE_URL}${url}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {})
      },
      body: JSON.stringify(data)
    })
    return res.json()
  },

  async delete(url) {
    const token = localStorage.getItem('token')
    const res = await fetch(`${BASE_URL}${url}`, {
      method: 'DELETE',
      headers: token ? { Authorization: `Bearer ${token}` } : {}
    })
    return res.json()
  },

  logout() {
    localStorage.removeItem('token')
  }
}

export default API