import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from infra.db import engine


# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generate_revenue_dashboard():

    sql = """

    SELECT
        dt,
        total_gmv
    FROM ads_revenue_dashboard
    ORDER BY dt

    """

    df = pd.read_sql(sql, engine)

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["dt"],
        df["total_gmv"],
        marker="o"
    )

    plt.title("GMV趋势图")

    plt.xlabel("日期")

    plt.ylabel("GMV")

    plt.xticks(rotation=45)

    plt.tight_layout()

    chart_path = (
            Path(__file__).parent
            / "charts"
            / "gmv_trend.png"
    )

    plt.savefig(chart_path)

    plt.close()

    print("GMV趋势图生成成功")


if __name__ == "__main__":

    generate_revenue_dashboard()