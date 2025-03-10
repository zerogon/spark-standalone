from pyspark.sql import SparkSession

# Spark 세션 생성
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .getOrCreate()

# Spark 버전 출력
print("Spark Version:", spark.version)
