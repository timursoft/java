def test_user_can_select_scores_to_share():
    """Test that user can select which scores to share."""
    # Arrange
    scores = [{'id': 1, 'score': 500}, {'id': 2, 'score': 1000}]
    selected_score_ids = [2]

    # Act
    selected_scores = select_scores_to_share(scores, selected_score_ids)

    # Assert
    assert len(selected_scores) == 1, "Expected one score to be selected, got {len(selected_scores)}"
    assert selected_scores[0]['score'] == 1000, "Expected selected score to be 1000, got {selected_scores[0]['score']}"