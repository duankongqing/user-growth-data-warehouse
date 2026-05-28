from sqlalchemy import text

from infra.db import engine


def check_duplicate_orders():

    sql = """

    SELECT
        order_id,
        COUNT(*) AS cnt
    FROM ods_orders
    GROUP BY order_id
    HAVING COUNT(*) > 1

    """

    with engine.begin() as conn:

        result = conn.execute(text(sql))

        rows = result.fetchall()

        print("重复订单数:", len(rows))


def check_negative_amount():

    sql = """

    SELECT *
    FROM ods_orders
    WHERE order_amount < 0

    """

    with engine.begin() as conn:

        result = conn.execute(text(sql))

        rows = result.fetchall()

        print("异常金额订单数:", len(rows))


if __name__ == "__main__":

    check_duplicate_orders()

    check_negative_amount()