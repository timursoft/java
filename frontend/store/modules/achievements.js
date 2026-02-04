import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  achievements: []
};

const mutations = {
  SET_ACHIEVEMENTS(state, achievements) {
    state.achievements = achievements;
  }
};

const actions = {
  async fetchAchievements({ commit }) {
    try {
      // Dummy API call simulation
      const achievements = [
        { id: 1, title: 'First Blood', description: 'First enemy defeated', date: '2023-10-01' },
        { id: 2, title: 'Marathon Runner', description: 'Completed a marathon', date: '2023-10-02' }
      ];
      commit('SET_ACHIEVEMENTS', achievements);
    } catch (error) {
      this.$log.error('Error fetching achievements: {}', error);
    }
  }
};

const getters = {
  achievements: (state) => state.achievements
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
