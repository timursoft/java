def test_feedback_collected_successfully(feedback_service):
    """Test feedback collection is successful."""
    # Arrange
    feedback_service.mock_feedback_collection(["Feedback 1", "Feedback 2"])
    
    # Act
    feedbacks = feedback_service.get_feedback()

    # Assert
    assert len(feedbacks) > 0, "Feedback should be collected successfully."