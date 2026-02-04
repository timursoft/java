import { createRouter, createWebHistory } from 'vue-router';
// existing imports

const routes = [
  // existing routes
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

// Potentially add new route or guard if needed

export default router;
