def test_snake_continues_moving_after_direction_change(snake):
    """
    Test that the snake continues moving after a direction change.
    """
    # Arrange
    snake.change_direction('left')
    snake.move()
    initial_positions = snake.get_positions()
    
    # Act
    snake.change_direction('down')
    snake.move()
    current_positions = snake.get_positions()
    
    # Assert
    assert initial_positions != current_positions, "Snake did not continue moving after direction change."