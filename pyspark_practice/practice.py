import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    os.environ["PYSPARK_PYTHON"] = sys.executable

    spark = (
        SparkSession.builder
        .appName("daily-pyspark-practice")
        .master("local[2]")
        .getOrCreate()
    )

    try:
        orders = spark.createDataFrame(
            [
                ("Ava", "books", 24.50),
                ("Ava", "games", 39.99),
                ("Noah", "books", 15.00),
                ("Noah", "games", 12.50),
            ],
            ["customer", "category", "amount"],
        )

        (
            orders
            .filter(F.col("amount") >= 20)
            .groupBy("category")
            .agg(F.sum("amount").alias("total_amount"))
            .orderBy("category")
            .show()
        )
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
