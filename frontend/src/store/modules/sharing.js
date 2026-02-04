import { log } from '../../utils/logger';

export const state = {
  // existing state
};

export const actions = {
  async shareOnFacebook({ commit }, leaderboardData) {
    try {
      const formattedData = this.formatForFacebook(leaderboardData);
      await this.apiShareOnFacebook(formattedData);
      log.info('Leaderboard shared on Facebook with data: {}', formattedData);
    } catch (error) {
      log.error('Failed to share leaderboard on Facebook: {}', error);
      throw error;
    }
  },

  formatForFacebook(leaderboardData) {
    return `Check out my leaderboard ranking: ${leaderboardData.rank}! Join me on this platform.`;
  },

  async apiShareOnFacebook(formattedData) {
    // Assume there's an existing API utility to handle HTTP requests
    const response = await apiClient.post('/share/facebook', { message: formattedData });
    if (!response.ok) {
      throw new Error('Failed to share on Facebook');
    }
  }
};
