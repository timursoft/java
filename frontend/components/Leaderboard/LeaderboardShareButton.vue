<template>
  <div>
    <button @click="shareOnInstagram">Share on Instagram</button>
    <!-- existing buttons -->
  </div>
</template>

<script>
export default {
  methods: {
    shareOnInstagram() {
      this.$store.dispatch('leaderboard/shareOnInstagram', this.leaderboardData);
    }
  },
  computed: {
    leaderboardData() {
      return this.$store.state.leaderboard.data;
    }
  }
}
</script>