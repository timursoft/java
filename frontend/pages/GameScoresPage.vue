<template>
  <div>
    <h1>Your Game Scores</h1>
    <ul>
      <li v-for="score in scores" :key="score.id">
        <input type="checkbox" :value="score.id" v-model="selectedScores" />
        {{ score.value }}
      </li>
    </ul>
    <SocialShareButton />
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import SocialShareButton from '@/components/SocialShareButton.vue';

export default {
  name: 'GameScoresPage',
  components: {
    SocialShareButton,
  },
  computed: {
    ...mapState({
      scores: state => state.scores.allScores,
      selectedScores: state => state.scores.selectedScores,
    }),
  },
  watch: {
    selectedScores(newScores) {
      this.updateSelectedScores(newScores);
    },
  },
  methods: {
    ...mapMutations(['updateSelectedScores']),
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
}
</style>
