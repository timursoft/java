<template>
  <div class="social-media-settings">
    <h2>Social Media Sharing Settings</h2>
    <div v-for="platform in platforms" :key="platform.id" class="platform-toggle">
      <label :for="platform.name">{{ platform.name }}</label>
      <input type="checkbox" :id="platform.name" v-model="selectedPlatforms" :value="platform.id" />
    </div>
    <button @click="saveSettings">Save</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  name: 'SocialMediaSettings',
  setup() {
    const store = useStore();
    const platforms = ref([]);
    const selectedPlatforms = ref(store.state.socialMediaSettings.selectedPlatforms);

    onMounted(() => {
      store.dispatch('socialMediaSettings/fetchPlatforms')
        .then((response) => {
          platforms.value = response;
        })
        .catch((error) => {
          console.error('Failed to fetch platforms', error);
        });
    });

    const saveSettings = () => {
      store.dispatch('socialMediaSettings/saveSettings', selectedPlatforms.value)
        .then(() => {
          console.log('Settings saved successfully');
        })
        .catch((error) => {
          console.error('Failed to save settings', error);
        });
    };

    return {
      platforms,
      selectedPlatforms,
      saveSettings,
    };
  },
});
</script>

<style scoped>
.social-media-settings {
  /* Use design tokens for consistency */
  padding: var(--spacing-medium);
  background-color: var(--background-color);
}

.platform-toggle {
  margin-bottom: var(--spacing-small);
}
</style>
