import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from infra.db import engine


# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generate_operation_dashboard():

    sql = """

    SELECT
        order_channel,
        total_gmv
    FROM dws_channel_conversion_1d

    """

    df = pd.read_sql(sql, engine)

    plt.figure(figsize=(10, 5))

    plt.bar(
        df["order_channel"],
        df["total_gmv"]
    )

    plt.title("渠道GMV分析")

    plt.xlabel("渠道")

    plt.ylabel("GMV")

    plt.xticks(rotation=15)

    plt.tight_layout()

    chart_path = (
            Path(__file__).parent
            / "charts"
            / "channel_gmv.png"
    )

    plt.savefig(chart_path)

    plt.savefig(chart_path)

    plt.close()

    print("渠道GMV图生成成功")


if __name__ == "__main__":

    generate_operation_dashboard()