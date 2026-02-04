<template>
  <div class="achievement-share-dialog">
    <h2>Select Achievements to Share</h2>
    <ul>
      <li v-for="achievement in achievements" :key="achievement.id">
        <label>
          <input type="checkbox" v-model="selectedAchievements" :value="achievement" />
          {{ achievement.title }}
        </label>
      </li>
    </ul>
    <button @click="shareAchievements">Share on Social Media</button>
    <p v-if="confirmationMessage">{{ confirmationMessage }}</p>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import SocialMediaIntegration from './SocialMediaIntegration.vue';
import { formatForSocialMedia } from '../utils/formatters';

export default {
  components: {
    SocialMediaIntegration
  },
  data() {
    return {
      selectedAchievements: [],
      confirmationMessage: ''
    };
  },
  computed: {
    ...mapState('achievements', ['achievements'])
  },
  methods: {
    ...mapActions('achievements', ['fetchAchievements']),
    async shareAchievements() {
      try {
        const formattedData = this.selectedAchievements.map(formatForSocialMedia);
        await this.$refs.socialMediaIntegration.share(formattedData);
        this.confirmationMessage = 'Achievements shared successfully!';
      } catch (error) {
        this.$log.error('Failed to share achievements: {}', error);
        this.confirmationMessage = 'Failed to share achievements.';
      }
    }
  },
  created() {
    this.fetchAchievements();
  }
};
</script>

<style scoped>
.achievement-share-dialog {
  padding: 20px;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
