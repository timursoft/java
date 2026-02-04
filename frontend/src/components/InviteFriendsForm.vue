<template>
  <div>
    <h3>Invite Friends</h3>
    <form @submit.prevent="sendInvitations">
      <div v-for="(email, index) in emails" :key="index">
        <input v-model="emails[index]" type="email" placeholder="Enter email" required />
        <button @click.prevent="removeEmailField(index)">Remove</button>
      </div>
      <button type="button" @click="addEmailField">Add Another Email</button>
      <button type="submit">Send Invitations</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      emails: [''],
    };
  },
  methods: {
    ...mapActions(['sendInvitations']),
    addEmailField() {
      this.emails.push('');
    },
    removeEmailField(index) {
      this.emails.splice(index, 1);
    },
    sendInvitations() {
      this.$store.dispatch('sendInvitations', this.emails);
    },
  },
};
</script>
