<template>
  <div class="avatar-selector">
    <h3>Select Your Avatar Base Model</h3>
    <ul>
      <li v-for="model in baseModels" :key="model.id">
        <button @click="selectBaseModel(model)">{{ model.name }}</button>
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'AvatarSelector',
  computed: {
    ...mapState('avatar', ['baseModels', 'error']),
  },
  methods: {
    ...mapActions('avatar', ['fetchBaseModels', 'selectBaseModel']),
  },
  created() {
    this.fetchBaseModels();
  },
};
</script>

<style scoped>
.avatar-selector {
  padding: 16px;
}
.error {
  color: red;
}
</style>