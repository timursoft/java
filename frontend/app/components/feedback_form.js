import React, { useState } from 'react';

const FeedbackForm = () => {
    const [feedback, setFeedback] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        // Assuming `submitFeedback` is a function that handles feedback submission
        submitFeedback(feedback);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="feedback">Your Feedback:</label>
            <textarea
                id="feedback"
                name="feedback"
                value={feedback}
                onChange={(e) => setFeedback(e.target.value)}
                required
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default FeedbackForm;
