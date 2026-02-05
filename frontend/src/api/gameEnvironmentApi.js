import axios from 'axios';

export async function fetchAssets() {
  try {
    const response = await axios.get('/api/environment/assets');
    return response.data;
  } catch (error) {
    console.error('Error fetching environment assets:', error);
    throw error;
  }
}
