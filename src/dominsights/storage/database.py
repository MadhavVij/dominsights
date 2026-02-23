import duckdb

from dominsights.config import settings


def get_connection():
    return duckdb.connect(str(settings.database_path))


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS interval_usage (
            timestamp TIMESTAMP PRIMARY KEY,
            consumption DOUBLE
        )
    """)
    conn.close()
