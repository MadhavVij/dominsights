from fastapi import FastAPI

from dominsights.analytics.insights import generate_insights
from dominsights.analytics.usage import daily_usage

app = FastAPI(title="DomInsights API")


@app.get("/usage/daily")
def get_daily():
    data = daily_usage()
    return [{"date": str(d), "kwh": float(v)} for d, v in data.items()]


@app.get("/insights")
def insights():
    return generate_insights()


@app.get("/nl/summary")
def natural_language_summary():
    """
    FUTURE RELEASE:
    Hook into local LLM to summarize insights.
    """
    return {"status": "Coming in v0.2 - LLM integration"}
