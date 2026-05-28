from pathlib import Path
from sqlalchemy import text

from infra.db import engine
from etl.logger import logger


dwd_path = (
    Path(__file__).parent.parent
    / "warehouse"
    / "dwd"
)


def execute_sql_file(sql_file):

    with open(
        sql_file,
        "r",
        encoding="utf-8"
    ) as f:

        sql = f.read()

    with engine.begin() as conn:

        # 一个文件多个SQL
        for statement in sql.split(";"):

            statement = statement.strip()

            if statement:

                conn.execute(text(statement))

    logger.info(f"[DWD] success: {sql_file}")


def run_dwd():

    logger.info("======== START DWD ========")

    sql_files = sorted(
        dwd_path.rglob("*.sql")
    )

    for sql_file in sql_files:

        execute_sql_file(sql_file)

    logger.info("======== FINISH DWD ========")