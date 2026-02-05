<template>
  <div>
    <h1>Feedback Form</h1>
    <form @submit.prevent="submitFeedback">
      <textarea v-model="feedbackText" placeholder="Enter your feedback"></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      feedbackText: ''
    };
  },
  methods: {
    submitFeedback() {
      if (!this.feedbackText) {
        alert('Please enter some feedback before submitting.');
        return;
      }
      // Call an API to submit feedback
      alert('Feedback submitted! Thank you.');
    }
  }
};
</script>

<style scoped>
textarea {
  width: 100%;
  height: 150px;
}
button {
  margin-top: 10px;
}
</style>