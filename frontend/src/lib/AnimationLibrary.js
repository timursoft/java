.animation-item {
  transition: transform 0.5s ease-out;
  will-change: transform;
}

@keyframes optimizedAnimation {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(50px);
  }
  100% {
    transform: translateX(0);
  }
}

.animation-container {
  animation: optimizedAnimation 1s infinite alternate;
}