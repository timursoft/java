<template>
  <div>
    <h1>Leaderboard</h1>
    <ul>
      <li v-for="entry in leaderboardEntries" :key="entry.playerId" :class="{ 'high-score': entry.isHighScore }">
        {{ entry.playerName }}: {{ entry.score }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      leaderboardEntries: []
    };
  },
  methods: {
    fetchLeaderboard() {
      // Fetch leaderboard entries from the API
      this.leaderboardEntries = this.getLeaderboardData();
    },
    getLeaderboardData() {
      // Dummy data for illustration
      return [
        { playerId: 1, playerName: 'Alice', score: 1500, isHighScore: true },
        { playerId: 2, playerName: 'Bob', score: 1200, isHighScore: false }
      ];
    }
  },
  mounted() {
    this.fetchLeaderboard();
  }
};
</script>

<style>
.high-score {
  font-weight: bold;
  color: red;
}
</style>