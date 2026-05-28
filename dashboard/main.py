from dashboard.revenue_dashboard import (
    generate_revenue_dashboard
)

from dashboard.user_growth_dashboard import (
    generate_user_dashboard
)

from dashboard.operation_dashboard import (
    generate_operation_dashboard
)


def main():

    print("开始生成Dashboard图表")

    generate_revenue_dashboard()

    generate_user_dashboard()

    generate_operation_dashboard()

    print("所有Dashboard图表生成完成")


if __name__ == "__main__":

    main()