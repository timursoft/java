import React from 'react';
import { usePlayerStats } from '../hooks/usePlayerStats';
import '../styles/hud.css';

const HUD = () => {
    const { health, score, time } = usePlayerStats();

    return (
        <div className="hud-container">
            <div className="hud-item">Health: {health}</div>
            <div className="hud-item">Score: {score}</div>
            <div className="hud-item">Time: {time}</div>
        </div>
    );
};

export default HUD;