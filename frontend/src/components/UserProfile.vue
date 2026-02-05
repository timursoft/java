<template>
  <div v-if="error" class="error">{{ error }}</div>
  <div v-else-if="user">
    <h1>{{ user.name }}</h1>
    <p>Email: {{ user.email }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      user: null,
      error: null
    }
  },
  async created() {
    try {
      const response = await axios.get(`/api/users/${this.$route.params.userId}`)
      this.user = response.data
    } catch (error) {
      this.error = error.response && error.response.data.detail ? error.response.data.detail : 'Failed to load user data'
    }
  }
}
</script>

<style scoped>
.error {
  color: red;
}
</style>