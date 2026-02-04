import { shareToInstagram } from '../../api/socialMediaShare';

const state = {
  data: {},
};

const actions = {
  async shareOnInstagram({ state }) {
    try {
      const formattedData = this._vm.$formatters.formatForInstagram(state.data);
      await shareToInstagram(formattedData);
      this._vm.$notify({ type: 'success', message: 'Shared successfully on Instagram!' });
    } catch (error) {
      this._vm.$notify({ type: 'error', message: 'Failed to share on Instagram.' });
    }
  },
};

export default {
  state,
  actions,
};