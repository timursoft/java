import React, { useEffect, useState } from 'react';

const GameView = () => {
    const [gameState, setGameState] = useState({});

    useEffect(() => {
        const socket = new WebSocket('ws://localhost:8080');

        socket.onmessage = (event) => {
            const updatedState = JSON.parse(event.data);
            setGameState(updatedState);
        };

        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            {/* Render game state here */}
        </div>
    );
};

export default GameView;
