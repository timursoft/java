<template>
  <div class="leaderboard-page">
    <LeaderboardShareButton :leaderboardData="leaderboardData" />
  </div>
</template>

<script>
import LeaderboardShareButton from '../components/LeaderboardShareButton.vue';

export default {
  name: 'LeaderboardPage',
  components: {
    LeaderboardShareButton
  },
  data() {
    return {
      leaderboardData: {
        rank: 1, // Example data
        // Additional data if necessary
      }
    };
  }
};
</script>

<style scoped>
/* Add any necessary styles */
</style>
