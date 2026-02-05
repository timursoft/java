import { fetchAssets } from '../../api/gameEnvironmentApi';

const state = {
  skyboxTexture: null,
  terrainHeightMap: null,
  lightingSettings: null,
};

const getters = {
  skyboxTexture: (state) => state.skyboxTexture,
  terrainHeightMap: (state) => state.terrainHeightMap,
  lightingSettings: (state) => state.lightingSettings,
};

const actions = {
  async fetchEnvironmentAssets({ commit }) {
    try {
      const assets = await fetchAssets();
      commit('setSkyboxTexture', assets.skybox);
      commit('setTerrainHeightMap', assets.terrain);
      commit('setLightingSettings', assets.lighting);
    } catch (error) {
      console.error('Failed to fetch environment assets:', error);
    }
  },
};

const mutations = {
  setSkyboxTexture(state, texture) {
    state.skyboxTexture = texture;
  },
  setTerrainHeightMap(state, heightMap) {
    state.terrainHeightMap = heightMap;
  },
  setLightingSettings(state, settings) {
    state.lightingSettings = settings;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
