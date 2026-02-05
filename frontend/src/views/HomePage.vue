<template>
  <div class="home-page">
    <NavBar/>
    <ButtonGroup :buttons="homeButtons"/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import ButtonGroup from '@/components/ButtonGroup.vue';

export default {
  name: 'HomePage',
  components: {
    NavBar,
    ButtonGroup,
  },
  data() {
    return {
      homeButtons: [
        { id: 1, label: 'Start', action: this.start },
        { id: 2, label: 'Settings', action: this.settings },
        { id: 3, label: 'Help', action: this.help },
      ],
    };
  },
  methods: {
    start() {
      console.log('Start action');
    },
    settings() {
      console.log('Settings action');
    },
    help() {
      console.log('Help action');
    },
  },
};
</script>

<style scoped>
.home-page {
  padding: 20px;
}
</style>