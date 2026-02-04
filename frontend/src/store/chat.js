import { createStore } from 'vuex';

export default createStore({
  state: {
    messages: [],
    showEmojiPalette: false
  },
  mutations: {
    addMessage(state, message) {
      state.messages.push(message);
    },
    toggleEmojiPalette(state) {
      state.showEmojiPalette = !state.showEmojiPalette;
    }
  },
  actions: {
    sendEmoji({ commit }, emoji) {
      // Simulate sending emoji over WebSocket
      commit('addMessage', { id: Date.now(), text: emoji });
      // Here you would have your WebSocket logic
    }
  }
});