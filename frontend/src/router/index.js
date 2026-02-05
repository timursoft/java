import Vue from 'vue';
import Router from 'vue-router';
import MainDashboard from '@/components/Dashboard/MainDashboard.vue';
import FeedbackAnalyticsDashboard from '@/components/Dashboard/FeedbackAnalyticsDashboard.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainDashboard',
      component: MainDashboard
    },
    {
      path: '/feedback-analytics',
      name: 'FeedbackAnalyticsDashboard',
      component: FeedbackAnalyticsDashboard
    }
  ]
});
