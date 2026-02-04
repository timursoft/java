<template>
  <div class="game-layout">
    <header class="header">
      <!-- Header content -->
    </header>
    <main class="main-content">
      <slot></slot>
    </main>
    <footer class="footer">
      <!-- Footer content -->
    </footer>
  </div>
</template>

<script>
export default {
  name: 'GameLayout',
  data() {
    return {
      isMobile: false
    };
  },
  mounted() {
    this.checkResponsive();
    window.addEventListener('resize', this.checkResponsive);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkResponsive);
  },
  methods: {
    checkResponsive() {
      this.isMobile = window.innerWidth <= 768;
    }
  }
};
</script>

<style scoped>
.game-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header, .footer {
  background-color: var(--color-primary);
  padding: 1rem;
  text-align: center;
}

.main-content {
  flex: 1;
  padding: 1rem;
}

@media (max-width: 768px) {
  .header, .footer {
    font-size: 0.8rem;
  }
}
</style>