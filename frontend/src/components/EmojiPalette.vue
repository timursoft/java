<template>
  <div class="emoji-palette">
    <emoji-mart @select="selectEmoji" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import { EmojiMart } from 'emoji-mart-vue';

export default defineComponent({
  components: { EmojiMart },
  setup() {
    const store = useStore();

    const selectEmoji = (emoji: any) => {
      store.dispatch('chat/sendEmoji', emoji.native);
    };

    return { selectEmoji };
  }
});
</script>

<style scoped>
@import './emoji.css';

.emoji-palette {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>