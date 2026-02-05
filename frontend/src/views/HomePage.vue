<template>
  <div class="home-page">
    <MainMenu v-if="isMenuVisible" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import MainMenu from '@/components/MainMenu.vue';

export default {
  components: {
    MainMenu
  },
  computed: {
    ...mapState({
      isMenuVisible: state => state.uiState.isMenuVisible
    })
  }
}
</script>

<style scoped>
.home-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}
</style>