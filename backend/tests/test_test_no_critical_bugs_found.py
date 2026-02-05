def test_no_critical_bugs_found(regression_test_results):
    """Verify that no critical or high priority bugs are found during regression testing."""
    critical_bugs = [bug for bug in regression_test_results if bug.priority in ['critical', 'high']]
    assert len(critical_bugs) == 0, "Critical or high priority bugs found during regression testing"