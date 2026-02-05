def test_uat_conducted_with_sufficient_users(uat_service):
    """Test UAT is conducted with at least 10 users."""
    # Arrange
    expected_user_count = 10
    uat_service.mock_users_conducted_uat(15)
    
    # Act
    user_count = uat_service.get_user_count()

    # Assert
    assert user_count >= expected_user_count, f"User count is {user_count}, expected at least {expected_user_count}"