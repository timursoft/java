<template>
  <nav class="responsive-menu">
    <ul>
      <li v-for="item in menuItems" :key="item.id">
        <a :href="item.link">{{ item.name }}</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'ResponsiveMenu',
  props: {
    menuItems: {
      type: Array,
      required: true
    }
  },
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
.responsive-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  background-color: var(--color-secondary);
  padding: 0.5rem 0;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: row;
}

li {
  margin: 0 0.5rem;
}

@media (max-width: 768px) {
  .responsive-menu {
    flex-direction: column;
    align-items: center;
  }

  ul {
    flex-direction: column;
  }

  li {
    margin: 0.5rem 0;
  }
}
</style>