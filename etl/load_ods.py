from sqlalchemy import text

from infra.db import engine

from etl.extract import (
    extract_users,
    extract_events,
    extract_orders
)

from etl.logger import logger


def load_table(df, table_name):

    try:

        with engine.begin() as conn:
            conn.execute(text(f"TRUNCATE TABLE {table_name}"))

        df.to_sql(
            table_name,
            con=engine,
            index=False,
            if_exists="append",
            chunksize=1000,
            method="multi"
        )

        logger.info(f"{table_name} load success")

    except Exception as e:

        logger.error(f"{table_name} load failed: {e}")

        raise


def load_ods():

    load_table(
        extract_users(),
        "ods_users"
    )

    load_table(
        extract_events(),
        "ods_events"
    )

    load_table(
        extract_orders(),
        "ods_orders"
    )


if __name__ == "__main__":

    load_ods()