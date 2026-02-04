import Vue from 'vue';
import Vuex from 'vuex';
import scoreService from '../api/scoreService';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    topScores: [],
    loading: false,
    error: null
  },
  mutations: {
    SET_LOADING(state, isLoading) {
      state.loading = isLoading;
    },
    SET_SCORES(state, scores) {
      state.topScores = scores;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  actions: {
    async fetchScores({ commit }) {
      commit('SET_LOADING', true);
      try {
        const scores = await scoreService.getTopScores();
        commit('SET_SCORES', scores);
        commit('SET_ERROR', null);
      } catch (error) {
        commit('SET_ERROR', 'Failed to load scores.');
      } finally {
        commit('SET_LOADING', false);
      }
    }
  }
});
