import { io } from 'socket.io-client';
import { getLogger } from '../../utils/logger';

const logger = getLogger('matchmakingApi');

const socket = io('http://localhost:4000'); // Assume backend runs on localhost:4000

export const fetchInitialStatus = () => async (dispatch) => {
    try {
        const response = await fetch('/api/matchmaking/status');
        const data = await response.json();
        dispatch(updateMatchmakingStatus(data.status));
    } catch (error) {
        logger.error('Failed to fetch initial matchmaking status: {}', error);
    }
};

export const listenForStatusUpdates = (callback) => {
    socket.on('matchmakingStatus', (status) => {
        callback(status);
    });
    return () => {
        socket.off('matchmakingStatus');
    };
};