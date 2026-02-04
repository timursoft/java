<template>
  <div class="avatar-customization">
    <h2>Customize Your Avatar</h2>
    <AvatarSelector />
    <div v-if="selectedBaseModel">
      <p>Selected Base Model: {{ selectedBaseModel.name }}</p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import AvatarSelector from '@/components/AvatarSelector.vue';

export default {
  name: 'AvatarCustomizationView',
  components: {
    AvatarSelector,
  },
  computed: {
    ...mapState('avatar', ['selectedBaseModel']),
  },
};
</script>

<style scoped>
.avatar-customization {
  padding: 24px;
}
</style>