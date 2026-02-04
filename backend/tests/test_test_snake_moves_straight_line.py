def test_snake_moves_straight_line(snake):
    """
    Test that the snake moves in a straight line when no input is received.
    """
    # Arrange
    initial_positions = snake.get_positions()
    
    # Act
    snake.move()
    current_positions = snake.get_positions()
    
    # Assert
    assert all(p1[0] == p2[0] or p1[1] == p2[1] for p1, p2 in zip(initial_positions, current_positions)), \
        "Snake did not move in a straight line."