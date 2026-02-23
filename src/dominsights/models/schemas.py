from datetime import date

from pydantic import BaseModel


class DailyUsage(BaseModel):
    date: date
    kwh: float


class Insights(BaseModel):
    average_daily_kwh: float
    peak_hour: int
    baseline_load_kwh: float
