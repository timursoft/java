<template>
  <div class="avatar-customization">
    <AvatarStyleSelector />
    <StylePreview />
  </div>
</template>

<script>
import AvatarStyleSelector from '@/components/AvatarStyleSelector.vue';
import StylePreview from '@/components/StylePreview.vue';

export default {
  name: 'AvatarCustomization',
  components: {
    AvatarStyleSelector,
    StylePreview,
  },
};
</script>

<style scoped>
.avatar-customization {
  /* Add styles as per the design system */
}
</style>
