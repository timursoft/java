<template>
  <div class="main-menu">
    <!-- Existing menu items -->
    <button @click="openFeedbackForm">Submit Feedback</button>
  </div>
</template>

<script>
export default {
  methods: {
    openFeedbackForm() {
      this.$router.push({ name: 'FeedbackForm' });
    }
  }
};
</script>

<style scoped>
.main-menu button {
  /* Styling for the button */
}
</style>