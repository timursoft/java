import axios from 'axios';

export const fetchPlatformsFromApi = async () => {
  try {
    const response = await axios.get('/api/social-media/platforms');
    return response.data;
  } catch (error) {
    console.error('API error fetching platforms:', error);
    throw error;
  }
};

export const saveSettingsToApi = async (selectedPlatforms) => {
  try {
    await axios.post('/api/social-media/settings', { platforms: selectedPlatforms });
  } catch (error) {
    console.error('API error saving settings:', error);
    throw error;
  }
};
