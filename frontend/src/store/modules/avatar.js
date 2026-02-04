import avatarApi from '@/api/avatarApi'

const state = {
  avatar: null
}

const mutations = {
  SET_AVATAR(state, avatar) {
    state.avatar = avatar
  }
}

const actions = {
  async saveAvatarToProfile({ commit }, avatarData) {
    try {
      const response = await avatarApi.saveAvatar(avatarData)
      if (response.success) {
        commit('SET_AVATAR', avatarData)
        return true
      }
    } catch (error) {
      console.error('Failed to save avatar:', error)
    }
    return false
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
