<template>
  <div>
    <h1>Invitation Status</h1>
    <ul>
      <li v-for="invitation in invitations" :key="invitation.id">
        {{ invitation.friendName }} - {{ invitation.status }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'InvitationStatus',
  computed: {
    ...mapState('invitations', ['invitations'])
  },
  created() {
    this.fetchInvitations();
  },
  methods: {
    ...mapActions('invitations', ['fetchInvitations'])
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 8px;
  border-bottom: 1px solid #ccc;
}
</style>