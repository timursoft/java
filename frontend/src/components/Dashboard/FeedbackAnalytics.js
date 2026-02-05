import React, { useContext, useEffect, useState } from 'react';
import { FeedbackContext } from '../../context/FeedbackContext';
import { DateFilter, CategoryFilter } from '../Filters';
import { ExportButton } from '../ExportButton';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { fetchFeedbackAnalytics } from '../../api/feedbackApi';
import './dashboard.module.css';

const FeedbackAnalytics = () => {
  const { state, dispatch } = useContext(FeedbackContext);
  const [analyticsData, setAnalyticsData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchFeedbackAnalytics(state.filters);
        setAnalyticsData(data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [state.filters]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading data</div>;

  return (
    <div className="feedback-analytics">
      <DateFilter />
      <CategoryFilter />
      <ExportButton data={analyticsData} />
      <LineChart
        width={500}
        height={300}
        data={analyticsData}
        margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="trend" stroke="#8884d8" />
        <Line type="monotone" dataKey="theme" stroke="#82ca9d" />
      </LineChart>
    </div>
  );
};

export default FeedbackAnalytics;