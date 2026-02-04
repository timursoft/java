<template>
  <div class="chat-window" v-if="visible">
    <div class="chat-messages">
      <div v-for="message in messages" :key="message.id" class="message">
        <span class="user">{{ message.user }}:</span>
        <span class="text">{{ message.text }}</span>
      </div>
    </div>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type your message..." />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useSocket } from '../services/socketService';

export default {
  name: 'GameChatWindow',
  props: {
    visible: Boolean
  },
  setup() {
    const messages = ref([]);
    const newMessage = ref('');
    const socket = useSocket();

    const sendMessage = () => {
      if (newMessage.value.trim() !== '') {
        socket.emit('send_message', { text: newMessage.value });
        newMessage.value = '';
      }
    };

    onMounted(() => {
      socket.on('receive_message', (message) => {
        messages.value.push(message);
      });
    });

    return { messages, newMessage, sendMessage };
  }
};
</script>

<style scoped>
.chat-window {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 300px;
  height: 400px;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  display: flex;
  flex-direction: column;
}
.chat-messages {
  flex: 1;
  overflow-y: auto;
}
.message {
  margin: 5px;
}
input {
  border: none;
  padding: 10px;
  background-color: #333;
  color: white;
}
</style>