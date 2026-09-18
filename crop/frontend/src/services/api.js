import axios from 'axios'

const api = axios.create({ baseURL: 'http://127.0.0.1:5000' })

export const predictDisease = async (file) => {
  const form = new FormData()
  form.append('file', file)
  return (await api.post('/api/predict/disease', form)).data
}

export const predictYield = async (data) => (await api.post('/api/predict/yield', data)).data
export const getHistory = async () => (await api.get('/api/predictions')).data
export default api
