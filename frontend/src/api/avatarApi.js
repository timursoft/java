import axios from 'axios'

export default {
  async saveAvatar(avatarData) {
    try {
      const response = await axios.post('/api/avatar', avatarData)
      return response.data
    } catch (error) {
      console.error('API call failed:', error)
      return { success: false }
    }
  }
}
