import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import apiClient from '../../api/apiClient';

export const fetchUserHistory = createAsyncThunk(
  'user/fetchUserHistory',
  async () => {
    const response = await apiClient.get('/user/history');
    return response.data;
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    profile: null,
    history: {
      scores: [],
      loading: false,
      error: null,
    },
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUserHistory.pending, (state) => {
        state.history.loading = true;
        state.history.error = null;
      })
      .addCase(fetchUserHistory.fulfilled, (state, action) => {
        state.history.scores = action.payload;
        state.history.loading = false;
      })
      .addCase(fetchUserHistory.rejected, (state, action) => {
        state.history.error = action.error.message;
        state.history.loading = false;
      });
  },
});

export const selectUserHistory = (state) => state.user.history;

export default userSlice.reducer;
