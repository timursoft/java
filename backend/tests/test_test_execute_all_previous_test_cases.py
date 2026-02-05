def test_execute_all_previous_test_cases(previous_test_cases):
    """Ensure all test cases from previous sprints are executed without errors."""
    for test_case in previous_test_cases:
        assert test_case.run() == 'success', f"Test case {test_case.name} failed"