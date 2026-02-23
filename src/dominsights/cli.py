import asyncio

import typer

from dominsights.auth.manager import get_client
from dominsights.services.ingestion import ingest_last_days
from dominsights.storage.database import init_db

app = typer.Typer()


@app.command()
def init():
    init_db()
    typer.echo("Database initialized.")


@app.command()
def ingest(days: int = 7):

    async def run():
        async with get_client() as client:
            count = await ingest_last_days(client, days)
            print(f"Ingested {count} records")

    asyncio.run(run())


@app.command()
def plot_daily():
    import matplotlib.pyplot as plt

    from dominsights.analytics.usage import daily_usage

    data = daily_usage()
    plt.plot(list(data.keys()), list(data.values))
    plt.xticks(rotation=45)
    plt.title("Daily Energy Usage")
    plt.tight_layout()
    plt.show()


@app.command()
def run_api():
    import uvicorn

    uvicorn.run("dominsights.api.main:app", reload=True)


if __name__ == "__main__":
    app()
