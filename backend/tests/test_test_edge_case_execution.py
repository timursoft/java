def test_edge_case_execution(edge_cases):
    """Test execution of edge cases to ensure stability."""
    for edge_case in edge_cases:
        assert edge_case.run() == 'success', f"Edge case {edge_case.name} failed"