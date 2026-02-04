<template>
  <div class="share-buttons">
    <button @click="shareOnFacebook" class="facebook-share-button">Share on Facebook</button>
  </div>
</template>

<script>
import SocialShareMixin from '../mixins/SocialShareMixin';

export default {
  name: 'LeaderboardShareButton',
  mixins: [SocialShareMixin],
  methods: {
    shareOnFacebook() {
      this.$store.dispatch('sharing/shareOnFacebook', this.leaderboardData)
        .then(() => {
          this.$notify({ type: 'success', message: 'Shared successfully on Facebook!' });
        })
        .catch((error) => {
          this.$notify({ type: 'error', message: 'Failed to share on Facebook' });
          this.$log.error('Error sharing on Facebook: {}', error);
        });
    }
  }
}
</script>

<style scoped>
.facebook-share-button {
  background-color: #3b5998;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}
</style>
