<template>
  <div class="game-chat">
    <div class="messages">
      <div v-for="message in messages" :key="message.id" class="message">
        <span>{{ message.text }}</span>
      </div>
    </div>
    <emoji-palette v-if="showEmojiPalette" />
    <button @click="toggleEmojiPalette">😀</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import { useStore } from 'vuex';
import EmojiPalette from './EmojiPalette.vue';

export default defineComponent({
  components: { EmojiPalette },
  setup() {
    const store = useStore();
    const messages = computed(() => store.state.chat.messages);
    const showEmojiPalette = computed(() => store.state.chat.showEmojiPalette);

    const toggleEmojiPalette = () => {
      store.commit('chat/toggleEmojiPalette');
    };

    return { messages, showEmojiPalette, toggleEmojiPalette };
  }
});
</script>

<style scoped>
.game-chat {
  position: relative;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.messages {
  max-height: 300px;
  overflow-y: auto;
  margin-bottom: 10px;
}
.message {
  margin-bottom: 5px;
}
</style>