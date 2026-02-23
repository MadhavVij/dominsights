import pandas as pd

from dominsights.storage.database import get_connection


def load_dataframe() -> pd.DataFrame:
    conn = get_connection()
    df = conn.execute("SELECT * FROM interval_usage").df()
    conn.close()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def daily_usage():
    df = load_dataframe()
    df["date"] = df["timestamp"].dt.date
    return df.groupby("date")["consumption"].sum()
