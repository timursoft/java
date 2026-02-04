import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUserHistory, selectUserHistory } from '../../store/userSlice';
import ScoreHistoryGraph from './ScoreHistoryGraph';
import csvExport from '../../utils/csvExport';

const UserProfilePage = () => {
  const dispatch = useDispatch();
  const userHistory = useSelector(selectUserHistory);

  useEffect(() => {
    dispatch(fetchUserHistory());
  }, [dispatch]);

  const handleExportCSV = () => {
    csvExport(userHistory.scores, 'historical_scores.csv');
  };

  return (
    <div className="user-profile-page">
      <h1>Your Profile</h1>
      {/* Other profile components */}
      <div className="score-history-section">
        <h2>Score History</h2>
        {userHistory.loading && <p>Loading...</p>}
        {userHistory.error && <p>Error loading scores</p>}
        {!userHistory.loading && !userHistory.error && (
          <>
            <ScoreHistoryGraph data={userHistory.scores} />
            <button onClick={handleExportCSV}>Export as CSV</button>
          </>
        )}
      </div>
    </div>
  );
};

export default UserProfilePage;