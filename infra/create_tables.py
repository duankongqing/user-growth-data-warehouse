from pathlib import Path
from sqlalchemy import text

from infra.db import engine
from etl.logger import logger

warehouse_path = (
    Path(__file__).parent.parent / "warehouse"
)


def execute_sql_file(sql_file):

    with open(
        sql_file,
        "r",
        encoding="utf-8"
    ) as f:

        sql = f.read()

    with engine.begin() as conn:

        # 一个文件可能有多个SQL
        for statement in sql.split(";"):

            statement = statement.strip()

            if statement:

                conn.execute(text(statement))

    logger.info(f"execute sql: {sql_file}")


def create_tables():

    layers = [
        "ods",
        "dwd",
        "dws",
        "ads"
    ]

    for layer in layers:

        layer_path = warehouse_path / layer

        sql_files = sorted(
            layer_path.rglob("*.sql")
        )

        for sql_file in sql_files:

            execute_sql_file(sql_file)


if __name__ == "__main__":

    create_tables()