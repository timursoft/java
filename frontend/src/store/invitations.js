import axios from 'axios';
import { logger } from '@/utils/logger';

const state = {
  invitations: [],
};

const mutations = {
  ADD_INVITATION(state, invitation) {
    state.invitations.push(invitation);
  },
};

const actions = {
  async sendInvitations({ commit }, emails) {
    try {
      const response = await axios.post('/api/invitations/send', { emails });
      response.data.forEach(invitation => {
        commit('ADD_INVITATION', invitation);
      });
      logger.info('Invitations sent successfully.');
    } catch (error) {
      logger.error('Failed to send invitations: {}', error.message);
    }
  },
};

export default {
  state,
  mutations,
  actions,
};
