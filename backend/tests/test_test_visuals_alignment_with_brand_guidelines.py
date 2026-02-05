def test_visuals_alignment_with_brand_guidelines(mock_brand_guidelines, mock_visuals):
    """Test that visuals are aligned with brand guidelines."""
    # Arrange
    visuals = mock_visuals()
    brand_guidelines = mock_brand_guidelines()

    # Act
    alignment_result = check_visual_alignment(visuals, brand_guidelines)

    # Assert
    assert alignment_result, "Visuals are not aligned with brand guidelines."