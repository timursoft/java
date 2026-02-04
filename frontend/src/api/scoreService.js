import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL;

export default {
  async getTopScores() {
    const response = await axios.get(`${API_URL}/scores/top`);
    return response.data;
  }
};
