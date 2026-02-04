<template>
  <div class="invitation-page">
    <h1>Invite Friends</h1>
    <p>Share this invitation link with your friends and invite them to join the game!</p>
    <ShareButton />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ShareButton from '@/components/ShareButton.vue';

export default defineComponent({
  components: { ShareButton }
});
</script>

<style scoped>
.invitation-page {
  padding: 20px;
  text-align: center;
}
</style>