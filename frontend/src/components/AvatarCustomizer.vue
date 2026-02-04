<template>
  <div>
    <h1>Customize your Avatar</h1>
    <!-- Avatar customization UI elements here -->
    <button @click="saveAvatar">Save Avatar</button>
    <p v-if="saveSuccess">Avatar saved successfully!</p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      saveSuccess: false
    }
  },
  methods: {
    ...mapActions(['saveAvatarToProfile']),
    async saveAvatar() {
      const avatarData = { /* collect avatar data from UI */ }
      const success = await this.saveAvatarToProfile(avatarData)
      this.saveSuccess = success
    }
  }
}
</script>
