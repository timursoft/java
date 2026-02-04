import React from 'react';
import PropTypes from 'prop-types';
import { Line } from 'react-chartjs-2';

const ScoreHistoryGraph = ({ data }) => {
  const chartData = {
    labels: data.map(entry => entry.date),
    datasets: [
      {
        label: 'Scores Over Time',
        data: data.map(entry => entry.score),
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const options = {
    responsive: true,
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'month',
        },
      },
    },
  };

  return <Line data={chartData} options={options} />;
};

ScoreHistoryGraph.propTypes = {
  data: PropTypes.arrayOf(
    PropTypes.shape({
      date: PropTypes.string.isRequired,
      score: PropTypes.number.isRequired,
    })
  ).isRequired,
};

export default ScoreHistoryGraph;
