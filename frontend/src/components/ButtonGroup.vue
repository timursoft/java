<template>
  <div class="button-group">
    <button v-for="button in buttons" :key="button.id" @click="button.action">
      {{ button.label }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'ButtonGroup',
  props: {
    buttons: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.button-group {
  display: flex;
  justify-content: space-between;
  gap: 16px;
}
</style>