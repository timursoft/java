const state = {
  isMenuVisible: true
};

const mutations = {
  TOGGLE_MENU(state) {
    state.isMenuVisible = !state.isMenuVisible;
  }
};

const actions = {
  toggleMenu({ commit }) {
    commit('TOGGLE_MENU');
  },
  openSettings() {
    // Logic to open settings
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};
