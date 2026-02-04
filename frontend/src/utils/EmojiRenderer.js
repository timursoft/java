import React from 'react';
import { Emoji } from 'emoji-mart';

const EmojiRenderer = {
    render: (text) => {
        // Split text to replace emojis with Emoji components
        const parts = text.split(/(\uD83D[\uDC00-\uDFFF]|\uD83E[\uDD00-\uDDFF])/g);
        return parts.map((part, index) => (
            part.match(/\uD83D[\uDC00-\uDFFF]|\uD83E[\uDD00-\uDDFF]/) ?
                <Emoji key={index} emoji={part} size={16} /> :
                <span key={index}>{part}</span>
        ));
    }
};

export default EmojiRenderer;
