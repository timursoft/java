import React from 'react';

const GameOptions = ({ onOptionSelect }) => {
  const handleTap = (event) => {
    const option = event.target.getAttribute('data-option');
    if (option) {
      onOptionSelect(option);
    }
  };

  return (
    <div className="game-options" onClick={handleTap}>
      <button data-option="option1">Option 1</button>
      <button data-option="option2">Option 2</button>
      <button data-option="option3">Option 3</button>
    </div>
  );
};

export default GameOptions;
