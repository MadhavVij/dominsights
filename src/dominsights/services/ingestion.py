from datetime import date, timedelta

import pandas as pd

from dominsights.config import settings
from dominsights.storage.database import get_connection


async def ingest_last_days(client, days: int = 7):
    end = date.today()
    start = end - timedelta(days=days)

    usage = await client.async_get_interval_usage(
        account_number=settings.account_number,
        meter_number=settings.meter_number,
        start_date=start,
        end_date=end,
    )

    df = pd.DataFrame([{"timestamp": u.timestamp, "consumption": u.consumption} for u in usage])

    conn = get_connection()
    conn.execute("BEGIN TRANSACTION")
    conn.register("df_view", df)
    conn.execute("""
        INSERT OR REPLACE INTO interval_usage
        SELECT * FROM df_view
    """)
    conn.execute("COMMIT")
    conn.close()

    return len(df)
