<template>
  <div class="feedback-form">
    <h2>Submit Feedback</h2>
    <form @submit.prevent="submitFeedback">
      <textarea v-model="feedbackText" placeholder="Enter your feedback"></textarea>
      <input type="file" @change="handleFileUpload">
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import Notification from './Notification.vue';

export default {
  components: { Notification },
  data() {
    return {
      feedbackText: '',
      screenshot: null
    };
  },
  methods: {
    ...mapActions(['submitFeedbackAction']),
    handleFileUpload(event) {
      this.screenshot = event.target.files[0];
    },
    async submitFeedback() {
      try {
        await this.submitFeedbackAction({
          text: this.feedbackText,
          screenshot: this.screenshot
        });
        this.$emit('notify', 'Feedback submitted successfully!');
      } catch (error) {
        this.$emit('notify', 'Failed to submit feedback. Please try again.');
      }
    }
  }
};
</script>

<style scoped>
.feedback-form {
  /* Styling for the feedback form */
}
textarea {
  width: 100%;
  height: 100px;
}
button {
  /* Styling for the submit button */
}
</style>