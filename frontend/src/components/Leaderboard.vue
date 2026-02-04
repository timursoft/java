<template>
  <div class="leaderboard">
    <h1>Leaderboard</h1>
    <ul>
      <li v-for="player in topScores" :key="player.username">
        <span>{{ player.username }}</span>: <span>{{ player.score }}</span>
      </li>
    </ul>
    <div v-if="loading">Loading...</div>
    <div v-if="error">Error loading scores. Please try again later.</div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Leaderboard',
  computed: {
    ...mapState({
      topScores: state => state.leaderboard.topScores,
      loading: state => state.leaderboard.loading,
      error: state => state.leaderboard.error
    })
  },
  sockets: {
    connect() {
      this.$store.dispatch('leaderboard/fetchScores');
    },
    scoreUpdate(data) {
      this.$store.commit('leaderboard/SET_SCORES', data);
    }
  }
};
</script>

<style scoped>
.leaderboard {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
</style>