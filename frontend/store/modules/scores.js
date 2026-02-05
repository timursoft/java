const state = {
  allScores: [],
  selectedScores: [],
};

const mutations = {
  setScores(state, scores) {
    state.allScores = scores;
  },
  updateSelectedScores(state, selectedScores) {
    state.selectedScores = selectedScores;
  },
};

const actions = {
  fetchScores({ commit }) {
    // Placeholder for fetching scores logic
    const scores = [{ id: 1, value: 100 }, { id: 2, value: 200 }];
    commit('setScores', scores);
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
