import axios from 'axios';

export async function fetchAvailableAccessories() {
  const response = await axios.get('/api/accessories');
  return response.data;
}
