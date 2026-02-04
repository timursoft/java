import avatarApi from '@/api/avatarApi';

const state = {
  baseModels: [],
  selectedBaseModel: null,
  error: null,
};

const mutations = {
  SET_BASE_MODELS(state, models) {
    state.baseModels = models;
  },
  SET_SELECTED_BASE_MODEL(state, model) {
    state.selectedBaseModel = model;
  },
  SET_ERROR(state, error) {
    state.error = error;
  },
};

const actions = {
  async fetchBaseModels({ commit }) {
    try {
      const models = await avatarApi.fetchBaseModels();
      commit('SET_BASE_MODELS', models);
    } catch (error) {
      commit('SET_ERROR', error.message);
    }
  },
  selectBaseModel({ commit }, model) {
    commit('SET_SELECTED_BASE_MODEL', model);
  },
};

const getters = {
  baseModels: state => state.baseModels,
  selectedBaseModel: state => state.selectedBaseModel,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};