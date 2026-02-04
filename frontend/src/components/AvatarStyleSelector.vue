<template>
  <div class="avatar-style-selector">
    <h2>Select Your Style</h2>
    <div v-if="styles.length">
      <ul>
        <li v-for="style in styles" :key="style.id">
          <button @click="selectStyle(style)">{{ style.name }}</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Loading styles...</p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AvatarStyleSelector',
  computed: {
    ...mapGetters('avatarStyles', ['getAvailableStyles']),
    styles() {
      return this.getAvailableStyles;
    },
  },
  methods: {
    ...mapActions('avatarStyles', ['fetchStyles', 'selectStyle']),
  },
  created() {
    this.fetchStyles();
  },
};
</script>

<style scoped>
.avatar-style-selector {
  /* Add styles as per the design system */
}
</style>
