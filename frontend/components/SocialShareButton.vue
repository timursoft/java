<template>
  <div>
    <button v-if="showShareButton" @click="shareScores" class="share-button">Share Scores</button>
    <p v-if="confirmationMessage" class="confirmation">{{ confirmationMessage }}</p>
  </div>
</template>

<script>
import formatSocialMedia from '@/utils/formatSocialMedia';
import { mapState } from 'vuex';

export default {
  name: 'SocialShareButton',
  data() {
    return {
      confirmationMessage: '',
    };
  },
  computed: {
    ...mapState({
      scores: state => state.scores.selectedScores,
    }),
    showShareButton() {
      return this.scores.length > 0;
    },
  },
  methods: {
    shareScores() {
      try {
        const formattedScores = formatSocialMedia(this.scores);
        // Assume shareToSocialMedia is a method that handles the actual sharing process
        this.$socialMediaIntegration.share(formattedScores);
        this.confirmationMessage = 'Scores shared successfully!';
      } catch (error) {
        this.$log.error('Error sharing scores: {}', error);
        this.confirmationMessage = 'Failed to share scores. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
.share-button {
  background-color: var(--button-bg-color);
  color: var(--button-text-color);
}
.confirmation {
  font-size: var(--confirmation-font-size);
  color: var(--confirmation-text-color);
}
</style>
