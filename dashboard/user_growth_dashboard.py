import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from infra.db import engine


# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generate_user_dashboard():

    sql = """

    SELECT
        dt,
        dau
    FROM ads_user_growth_dashboard
    ORDER BY dt

    """

    df = pd.read_sql(sql, engine)

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["dt"],
        df["dau"],
        marker="o"
    )

    plt.title("DAU趋势图")

    plt.xlabel("日期")

    plt.ylabel("DAU")

    plt.xticks(rotation=45)

    plt.tight_layout()

    chart_path = (
            Path(__file__).parent
            / "charts"
            / "dau_trend.png"
    )

    plt.savefig(chart_path)

    plt.close()

    print("DAU趋势图生成成功")


if __name__ == "__main__":

    generate_user_dashboard()