import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchInitialStatus, listenForStatusUpdates } from '../../api/matchmakingApi';
import { updateMatchmakingStatus } from '../../store/matchmaking';
import './MatchmakingStatus.module.css';

const MatchmakingStatus = () => {
    const dispatch = useDispatch();
    const status = useSelector(state => state.matchmaking.status);

    useEffect(() => {
        dispatch(fetchInitialStatus());
        const unsubscribe = listenForStatusUpdates((newStatus) => {
            dispatch(updateMatchmakingStatus(newStatus));
        });

        return () => unsubscribe();
    }, [dispatch]);

    return (
        <div className={`matchmaking-status ${status}`}>
            {status === 'searching' && <p>Searching for an opponent...</p>}
            {status === 'matched' && <p>You have been matched!</p>}
        </div>
    );
};

export default MatchmakingStatus;