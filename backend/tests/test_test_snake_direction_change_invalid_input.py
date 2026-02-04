def test_snake_direction_change_invalid_input(snake):
    """
    Test that the snake does not change direction on invalid input.
    """
    # Arrange
    initial_direction = snake.direction
    
    # Act
    with pytest.raises(ValueError, match="Invalid direction"):
        snake.change_direction('invalid_direction')
    
    # Assert
    assert snake.direction == initial_direction, "Snake direction changed on invalid input."