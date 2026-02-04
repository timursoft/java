<template>
  <div>
    <!-- Existing share options -->
    <button @click="$emit('select', 'instagram')">Instagram</button>
  </div>
</template>

<script>
export default {
  methods: {
    selectOption(option) {
      this.$emit('select', option);
    }
  }
}
</script>