import axios from 'axios';

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL;

export default {
  async getStyles() {
    try {
      const response = await axios.get(`${API_BASE_URL}/avatar/styles`);
      return response;
    } catch (error) {
      console.error('Error fetching styles:', error);
      throw error;
    }
  },
};
