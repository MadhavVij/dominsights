from dominsights.analytics.usage import load_dataframe


def generate_insights():
    df = load_dataframe()

    avg_daily = df.groupby(df["timestamp"].dt.date)["consumption"].sum().mean()
    peak_hour = df.groupby(df["timestamp"].dt.hour)["consumption"].mean().idxmax()
    baseline = df["consumption"].min()

    return {
        "average_daily_kwh": round(avg_daily, 2),
        "peak_hour": int(peak_hour),
        "baseline_load_kwh": round(baseline, 3),
    }
