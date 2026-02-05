import Vue from 'vue';
import Vuex from 'vuex';
import feedbackService from '@/api/feedbackService';

Vue.use(Vuex);

export default {
  namespaced: true,
  state: {
    feedbackData: [],
    categories: [],
    loading: false,
    error: null
  },
  mutations: {
    SET_FEEDBACK_DATA(state, data) {
      state.feedbackData = data;
    },
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    },
    SET_LOADING(state, isLoading) {
      state.loading = isLoading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  actions: {
    async fetchFeedbackData({ commit }, { category, startDate, endDate }) {
      commit('SET_LOADING', true);
      try {
        const { data } = await feedbackService.getFeedbackAnalytics(category, startDate, endDate);
        commit('SET_FEEDBACK_DATA', data);
      } catch (error) {
        commit('SET_ERROR', error);
      } finally {
        commit('SET_LOADING', false);
      }
    }
  }
};
