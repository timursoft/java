import { Module } from 'vuex';
import apiService from '@/api/apiService';
import { logError } from '@/utils/logger';

const state = {
  availableStyles: [],
  selectedStyle: null,
};

const getters = {
  getAvailableStyles: (state) => state.availableStyles,
  getSelectedStyle: (state) => state.selectedStyle,
};

const actions = {
  async fetchStyles({ commit }) {
    try {
      const response = await apiService.getStyles();
      commit('setAvailableStyles', response.data);
    } catch (error) {
      logError('Error fetching styles', error);
    }
  },
  selectStyle({ commit }, style) {
    commit('setSelectedStyle', style);
  },
};

const mutations = {
  setAvailableStyles(state, styles) {
    state.availableStyles = styles;
  },
  setSelectedStyle(state, style) {
    state.selectedStyle = style;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
