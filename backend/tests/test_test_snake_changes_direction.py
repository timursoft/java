def test_snake_changes_direction(snake):
    """
    Test that the snake changes direction when input is received.
    """
    # Arrange
    initial_direction = snake.direction
    
    # Act
    snake.change_direction('up')
    snake.move()
    
    # Assert
    assert snake.direction == 'up', "Snake did not change direction to up."