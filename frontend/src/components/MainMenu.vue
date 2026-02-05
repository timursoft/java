<template>
  <nav class="main-menu">
    <ul>
      <li><button @click="startGame" class="menu-button">Play</button></li>
      <li><button @click="openSettings" class="menu-button">Settings</button></li>
      <li><button @click="exitGame" class="menu-button">Exit</button></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'MainMenu',
  methods: {
    startGame() {
      this.$store.dispatch('game/start');
    },
    openSettings() {
      this.$store.dispatch('uiState/openSettings');
    },
    exitGame() {
      this.$store.dispatch('game/exit');
    }
  }
}
</script>

<style scoped>
@import '@/styles/designTokens.scss';

.main-menu {
  display: flex;
  flex-direction: column;
  align-items: center;
  .menu-button {
    margin: 10px;
    padding: 10px 20px;
    font-size: $font-size-large;
    color: $color-primary;
    background-color: $color-background;
    border: none;
    border-radius: $border-radius-small;
    transition: background-color 0.3s ease;
    &:hover {
      background-color: $color-hover;
    }
  }
}
</style>