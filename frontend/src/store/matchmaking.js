import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    status: 'idle',
};

const matchmakingSlice = createSlice({
    name: 'matchmaking',
    initialState,
    reducers: {
        updateMatchmakingStatus(state, action) {
            state.status = action.payload;
        },
    },
});

export const { updateMatchmakingStatus } = matchmakingSlice.actions;

export default matchmakingSlice.reducer;