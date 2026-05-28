from etl.logger import logger

from infra.create_tables import create_tables

from etl.load_ods import load_ods

from etl.ods_to_dwd import run_dwd

from etl.dwd_to_dws import run_dws

from etl.dws_to_ads import run_ads

from etl.quality import (
    check_duplicate_orders,
    check_negative_amount
)


def main():

    try:

        logger.info("========== ETL START ==========")

        # 1. 创建表
        logger.info("开始创建仓库表")

        create_tables()

        logger.info("仓库表创建完成")

        # 2. 导入ODS
        logger.info("开始加载ODS数据")

        load_ods()

        logger.info("ODS数据加载完成")

        # 3. ODS -> DWD
        logger.info("开始执行DWD层")

        run_dwd()

        logger.info("DWD层执行完成")

        # 4. DWD -> DWS
        logger.info("开始执行DWS层")

        run_dws()

        logger.info("DWS层执行完成")

        # 5. DWS -> ADS
        logger.info("开始执行ADS层")

        run_ads()

        logger.info("ADS层执行完成")

        # 6. 数据质量检查
        logger.info("开始数据质量检查")

        check_duplicate_orders()

        check_negative_amount()

        logger.info("数据质量检查完成")

        logger.info("========== ETL FINISH ==========")

        print("ETL流程执行成功")

    except Exception as e:

        logger.error(f"ETL执行失败: {e}")

        print("ETL流程执行失败")


if __name__ == "__main__":

    main()