import { fetchAvailableAccessories } from '@/api/avatarApi';

export const state = {
  accessories: [],
  selectedAccessories: [],
};

export const mutations = {
  SET_ACCESSORIES(state, accessories) {
    state.accessories = accessories;
  },
  SELECT_ACCESSORY(state, accessoryId) {
    if (!state.selectedAccessories.includes(accessoryId)) {
      state.selectedAccessories.push(accessoryId);
    }
  },
};

export const actions = {
  async fetchAccessories({ commit }) {
    try {
      const accessories = await fetchAvailableAccessories();
      commit('SET_ACCESSORIES', accessories);
    } catch (error) {
      console.error('Failed to fetch accessories:', error);
      throw error;
    }
  },
  selectAccessory({ commit }, accessoryId) {
    commit('SELECT_ACCESSORY', accessoryId);
  },
};

export const getters = {
  availableAccessories: state => state.accessories,
  selectedAccessories: state => state.selectedAccessories,
};