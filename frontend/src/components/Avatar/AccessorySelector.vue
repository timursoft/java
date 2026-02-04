<template>
  <div>
    <div v-if="loading" class="loading-spinner">Loading accessories...</div>
    <div v-if="error" class="error-message">Failed to load accessories. Please try again later.</div>
    <div v-if="!loading && !error">
      <div v-for="category in categorizedAccessories" :key="category.name" class="accessory-category">
        <h3>{{ category.name }}</h3>
        <div class="accessory-list">
          <div 
            v-for="accessory in category.accessories" 
            :key="accessory.id" 
            :class="['accessory-item', { selected: isSelected(accessory) }]"
            @click="selectAccessory(accessory)"
          >
            <img :src="accessory.previewUrl" :alt="accessory.name" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'AccessorySelector',
  data() {
    return {
      loading: true,
      error: false,
    };
  },
  computed: {
    ...mapState('avatar', ['accessories']),
    categorizedAccessories() {
      const categories = {};
      this.accessories.forEach(accessory => {
        if (!categories[accessory.category]) {
          categories[accessory.category] = [];
        }
        categories[accessory.category].push(accessory);
      });
      return Object.entries(categories).map(([name, accessories]) => ({ name, accessories }));
    }
  },
  methods: {
    ...mapActions('avatar', ['fetchAccessories', 'selectAccessory']),
    isSelected(accessory) {
      return this.$store.state.avatar.selectedAccessories.includes(accessory.id);
    }
  },
  async mounted() {
    try {
      await this.fetchAccessories();
    } catch (e) {
      this.error = true;
    } finally {
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.loading-spinner {
  text-align: center;
  font-size: 1.5em;
}
.error-message {
  color: red;
  text-align: center;
}
.accessory-category {
  margin-bottom: 20px;
}
.accessory-list {
  display: flex;
  flex-wrap: wrap;
}
.accessory-item {
  margin: 5px;
  cursor: pointer;
  transition: transform 0.2s;
}
.accessory-item.selected {
  border: 2px solid #007bff;
  transform: scale(1.1);
}
</style>
