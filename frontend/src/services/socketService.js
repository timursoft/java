import { io } from 'socket.io-client';

let socket;

export function useSocket() {
  if (!socket) {
    socket = io(process.env.VUE_APP_SOCKET_URL);

    socket.on('connect', () => {
      console.log('Connected to chat server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from chat server');
    });
  }

  return socket;
}
