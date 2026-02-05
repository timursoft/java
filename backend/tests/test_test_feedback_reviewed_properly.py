def test_feedback_reviewed_properly(feedback_service):
    """Test feedback is reviewed properly."""
    # Arrange
    feedback_service.mock_feedback_review(["Feedback 1", "Feedback 2"])
    
    # Act
    reviewed_feedbacks = feedback_service.review_feedback()

    # Assert
    assert all(f in reviewed_feedbacks for f in ["Feedback 1", "Feedback 2"]), "All feedback should be reviewed properly."