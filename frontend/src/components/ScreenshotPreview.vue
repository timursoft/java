<template>
  <div class="screenshot-preview">
    <img v-for="screenshot in screenshots" :key="screenshot.name" :src="screenshot.url" :alt="screenshot.altText" />
  </div>
</template>

<script>
export default {
  name: 'ScreenshotPreview',
  props: {
    screenshots: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.screenshot-preview {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.screenshot-preview img {
  margin: 10px;
  max-width: 100%;
  height: auto;
}
</style>
