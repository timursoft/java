<template>
  <div>
    <!-- Main game page with updated game features -->
    <GameFeature />
  </div>
</template>

<script>
import GameFeature from '../components/GameFeature.vue';
import { mapActions } from 'vuex';

export default {
  components: {
    GameFeature
  },
  created() {
    this.initializePlatform();
  },
  methods: {
    ...mapActions('gameFeatures', ['initializePlatform'])
  }
};
</script>

<style scoped>
/* Add any specific styles for GamePage if needed */
</style>