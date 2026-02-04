import React, { useState, useEffect } from 'react';
import PlatformDetector from '../utils/PlatformDetector';
import EmojiRenderer from '../utils/EmojiRenderer';
import '../styles/ChatStyles.css';

const ChatComponent = () => {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simulate fetching messages
        setTimeout(() => {
            setMessages(['Hello 👋', 'How are you? 😊']);
            setLoading(false);
        }, 1000);
    }, []);

    if (loading) {
        return <div className="chat-loading">Loading...</div>;
    }

    return (
        <div className={`chat-container ${PlatformDetector.getPlatformClass()}`}>
            {messages.map((msg, index) => (
                <div key={index} className="chat-message">
                    {EmojiRenderer.render(msg)}
                </div>
            ))}
        </div>
    );
};

export default ChatComponent;
