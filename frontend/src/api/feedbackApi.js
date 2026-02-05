import axios from 'axios';

export const fetchFeedbackAnalytics = async (filters) => {
  try {
    const response = await axios.get('/api/feedback/analytics', { params: filters });
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch feedback analytics');
  }
};