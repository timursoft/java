import Vue from 'vue';
import Router from 'vue-router';
import AchievementShareDialog from '@/components/AchievementShareDialog.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/share-achievements',
      name: 'ShareAchievements',
      component: AchievementShareDialog
    }
  ]
});
