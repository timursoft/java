def test_snake_speed_consistent(snake):
    """
    Test that the snake speed remains consistent across moves.
    """
    # Arrange
    initial_time = time.time()
    snake.move()
    
    # Act
    first_move_duration = time.time() - initial_time
    
    # Arrange
    initial_time = time.time()
    snake.move()
    
    # Act
    second_move_duration = time.time() - initial_time

    # Assert
    assert abs(first_move_duration - second_move_duration) < 0.01, "Snake speed is not consistent."