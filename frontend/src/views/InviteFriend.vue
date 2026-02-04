<template>
  <div class="invite-friend">
    <h2>Invite a Friend</h2>
    <input v-model="friendUsername" placeholder="Enter friend's username" />
    <button @click="inviteFriend">Invite</button>
    <div v-if="message" class="message">{{ message }}</div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      friendUsername: '',
      message: ''
    }
  },
  methods: {
    ...mapActions(['sendInvitation']),
    async inviteFriend() {
      try {
        await this.sendInvitation({ friendUsername: this.friendUsername });
        this.message = 'Invitation sent successfully!';
      } catch (error) {
        this.message = 'Failed to send invitation.';
      }
    }
  }
}
</script>

<style scoped>
.invite-friend {
  /* Add styles here */
}
.message {
  margin-top: 10px;
  color: red;
}
</style>