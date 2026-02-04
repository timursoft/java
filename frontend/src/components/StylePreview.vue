<template>
  <div class="style-preview">
    <h2>Style Preview</h2>
    <div v-if="selectedStyle">
      <p>Previewing: {{ selectedStyle.name }}</p>
      <!-- Additional preview display logic goes here -->
    </div>
    <div v-else>
      <p>No style selected.</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'StylePreview',
  computed: {
    ...mapGetters('avatarStyles', ['getSelectedStyle']),
    selectedStyle() {
      return this.getSelectedStyle;
    },
  },
};
</script>

<style scoped>
.style-preview {
  /* Add styles as per the design system */
}
</style>
