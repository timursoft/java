const state = {
  link: ''
};

const mutations = {
  setLink(state, link) {
    state.link = link;
  }
};

const actions = {
  generateInvitationLink({ commit }) {
    const baseUrl = process.env.VUE_APP_BASE_URL || 'http://localhost:8080';
    const invitationLink = `${baseUrl}/register?referral=yourReferralCode`;
    commit('setLink', invitationLink);
  }
};

const getters = {
  invitationLink: state => state.link
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};