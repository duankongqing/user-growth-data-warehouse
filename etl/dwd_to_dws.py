from pathlib import Path
from sqlalchemy import text

from infra.db import engine
from etl.logger import logger


dws_path = (
    Path(__file__).parent.parent
    / "warehouse"
    / "dws"
)


def execute_sql_file(sql_file):

    with open(
        sql_file,
        "r",
        encoding="utf-8"
    ) as f:

        sql = f.read()

    with engine.begin() as conn:

        for statement in sql.split(";"):

            statement = statement.strip()

            if statement:

                conn.execute(text(statement))

    logger.info(f"[DWS] success: {sql_file}")


def run_dws():

    logger.info("======== START DWS ========")

    sql_files = sorted(
        dws_path.rglob("*.sql")
    )

    for sql_file in sql_files:

        execute_sql_file(sql_file)

    logger.info("======== FINISH DWS ========")