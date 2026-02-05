def test_user_select_scores_invalid_id():
    """Test that selecting a score with an invalid ID raises an exception."""
    # Arrange
    scores = [{'id': 1, 'score': 500}, {'id': 2, 'score': 1000}]
    selected_score_ids = [3]  # Invalid ID

    # Act & Assert
    with pytest.raises(ValueError, match="Invalid score ID"): 
        select_scores_to_share(scores, selected_score_ids)