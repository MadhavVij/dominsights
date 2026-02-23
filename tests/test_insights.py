from dominsights.analytics.insights import generate_insights


def test_insights_structure():
    result = generate_insights()
    assert "average_daily_kwh" in result
    assert "peak_hour" in result
