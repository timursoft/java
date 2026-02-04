import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default {
  namespaced: true,
  state: {
    featureAEnabled: true,
    featureBEnabled: true,
    mobileFeatureEnabled: false,
    webFeatureEnabled: false,
    isMobile: false  // Should be set based on platform detection
  },
  mutations: {
    setMobileFeatureEnabled(state, enabled) {
      state.mobileFeatureEnabled = enabled;
    },
    setWebFeatureEnabled(state, enabled) {
      state.webFeatureEnabled = enabled;
    },
    detectPlatform(state) {
      state.isMobile = /Mobi|Android/i.test(navigator.userAgent);
    }
  },
  actions: {
    initializePlatform({ commit }) {
      commit('detectPlatform');
    }
  }
};