def test_no_feedback_collected(feedback_service):
    """Test no feedback collected raises exception."""
    # Arrange
    feedback_service.mock_feedback_collection([])

    # Act and Assert
    with pytest.raises(ValueError, match="No feedback collected"):
        feedback_service.get_feedback()