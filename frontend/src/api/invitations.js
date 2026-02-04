import axios from 'axios';

export const fetchInvitations = async () => {
  try {
    const response = await axios.get('/api/invitations');
    return response.data;
  } catch (error) {
    console.error('API Error fetching invitations:', error);
    throw error;
  }
};