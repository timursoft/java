import Vue from 'vue';
import Vuex from 'vuex';
import avatarStyles from './avatarStyles';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    avatarStyles,
  },
});
