<template>
  <div>
    <vue-social-sharing
      class="share-button"
      :url="shareUrl"
      :title="shareTitle"
      inline-template>
      <button v-for="network in networks" :key="network" @click="$refs[network].share()">
        Share on {{ network }}
      </button>
    </vue-social-sharing>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import vueSocialSharing from 'vue-social-sharing';
import { useStore } from 'vuex';

export default defineComponent({
  components: { vueSocialSharing },
  setup() {
    const store = useStore();
    const networks = ref(['Facebook', 'Twitter', 'LinkedIn']);
    const shareUrl = computed(() => store.state.invitation.link);
    const shareTitle = 'Invite your friends to join the game!';

    return { networks, shareUrl, shareTitle };
  }
});
</script>

<style scoped>
.share-button {
  margin: 10px;
  padding: 10px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
}
</style>