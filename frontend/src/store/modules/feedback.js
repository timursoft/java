import axios from 'axios';

const state = {
  feedbacks: []
};

const mutations = {
  ADD_FEEDBACK(state, feedback) {
    state.feedbacks.push(feedback);
  }
};

const actions = {
  async submitFeedbackAction({ commit }, { text, screenshot }) {
    try {
      const formData = new FormData();
      formData.append('text', text);
      if (screenshot) {
        formData.append('screenshot', screenshot);
      }
      const response = await axios.post('/api/feedback', formData);
      commit('ADD_FEEDBACK', response.data);
    } catch (error) {
      // Handle error
      throw new Error('Error submitting feedback');
    }
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};
