import React, { useEffect } from 'react';
import { useTapHandler } from '../hooks/useTapHandler';
import { observer } from 'mobx-react';

const GameInteraction = observer(() => {
  const { handleTap, handleDoubleTap } = useTapHandler();

  useEffect(() => {
    // Initialize tap event listeners
    document.addEventListener('tap', handleTap);
    document.addEventListener('doubleTap', handleDoubleTap);

    return () => {
      document.removeEventListener('tap', handleTap);
      document.removeEventListener('doubleTap', handleDoubleTap);
    };
  }, [handleTap, handleDoubleTap]);

  return (
    <div className="game-interaction">
      {/* Game interaction components */}
    </div>
  );
});

export default GameInteraction;
