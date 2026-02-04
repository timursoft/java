import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    invitations: []
  },
  mutations: {
    SET_INVITATIONS(state, invitations) {
      state.invitations = invitations;
    }
  },
  actions: {
    async fetchInvitations({ commit }) {
      try {
        const response = await axios.get('/api/invitations');
        commit('SET_INVITATIONS', response.data);
      } catch (error) {
        console.error('Error fetching invitations:', error);
      }
    }
  }
});