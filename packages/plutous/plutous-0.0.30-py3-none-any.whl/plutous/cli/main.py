from loguru import logger
from typer import Typer

app = Typer()
apps = []

try:
    from plutous.trade.cli import main as trade

    apps.append(trade.app)
except ImportError as e:
    logger.warning(e)

for a in apps:
    app.add_typer(a)


@app.command()
def start_server(
    host: str = "0.0.0.0",
    port: int = 8080,
    workers: int = 2,
    reload: bool = True,
):
    import uvicorn

    from plutous.config import CONFIG

    if CONFIG.sentry_dsn:
        import sentry_sdk

        sentry_sdk.init(CONFIG.sentry_dsn)

    uvicorn.run(
        "plutous.app.main:app",
        host=host,
        port=port,
        workers=workers,
        reload=reload,
    )


if __name__ == "__main__":
    app()
