import axios from 'axios';

export default {
  async getFeedbackAnalytics(category, startDate, endDate) {
    try {
      const response = await axios.get('/api/feedback/analytics', {
        params: { category, startDate, endDate }
      });
      return response.data;
    } catch (error) {
      throw new Error('Error fetching feedback analytics: ' + error);
    }
  }
};
