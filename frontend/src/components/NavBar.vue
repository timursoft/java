<template>
  <nav class="nav-bar">
    <ButtonGroup :buttons="navButtons"/>
  </nav>
</template>

<script>
import ButtonGroup from '@/components/ButtonGroup.vue';

export default {
  name: 'NavBar',
  components: {
    ButtonGroup,
  },
  data() {
    return {
      navButtons: [
        { id: 1, label: 'Home', action: this.goHome },
        { id: 2, label: 'Profile', action: this.goProfile },
        { id: 3, label: 'Logout', action: this.logout },
      ],
    };
  },
  methods: {
    goHome() {
      console.log('Navigate to home');
    },
    goProfile() {
      console.log('Navigate to profile');
    },
    logout() {
      console.log('Logging out');
    },
  },
};
</script>

<style scoped>
.nav-bar {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}
</style>