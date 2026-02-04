<template>
  <div>
    <button @click="shareOnTwitter" v-if="canShareOnTwitter">Share on Twitter</button>
    <!-- Existing share buttons -->
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import SocialSharing from 'vue-social-sharing';

export default defineComponent({
  components: {
    SocialSharing
  },
  setup() {
    const store = useStore();
    const canShareOnTwitter = true; // Add logic to determine if sharing is possible

    const shareOnTwitter = () => {
      const rankingText = store.getters['leaderboard/getFormattedRankingForTwitter'];
      store.dispatch('leaderboard/shareOnTwitter', rankingText);
    };

    return { canShareOnTwitter, shareOnTwitter };
  }
});
</script>

<style scoped>
button {
  /* Add styling */
}
</style>