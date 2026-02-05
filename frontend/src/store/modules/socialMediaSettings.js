import { Module } from 'vuex';
import { fetchPlatformsFromApi, saveSettingsToApi } from '@/api/socialMediaApi';

const state = {
  selectedPlatforms: [],
};

const mutations = {
  setPlatforms(state, platforms) {
    state.selectedPlatforms = platforms;
  },
};

const actions = {
  async fetchPlatforms({ commit }) {
    try {
      const platforms = await fetchPlatformsFromApi();
      commit('setPlatforms', platforms);
      return platforms;
    } catch (error) {
      console.error('Error fetching platforms:', error);
      throw error;
    }
  },
  async saveSettings({ state }) {
    try {
      await saveSettingsToApi(state.selectedPlatforms);
      console.log('Settings saved');
    } catch (error) {
      console.error('Error saving settings:', error);
      throw error;
    }
  },
};

export const socialMediaSettings = {
  namespaced: true,
  state,
  mutations,
  actions,
};
