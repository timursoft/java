<template>
  <div>
    <h2>Customize Your Avatar</h2>
    <AvatarPreview />
    <AccessorySelector />
  </div>
</template>

<script>
import AvatarPreview from '@/components/Avatar/AvatarPreview.vue';
import AccessorySelector from '@/components/Avatar/AccessorySelector.vue';

export default {
  name: 'AvatarCustomization',
  components: {
    AvatarPreview,
    AccessorySelector,
  },
};
</script>

<style scoped>
/* Add any additional styling needed for layout */
</style>
