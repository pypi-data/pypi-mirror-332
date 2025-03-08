import os
from pyspark.sql import SparkSession

__SC__ = None  # Global SparkContext (Singleton-like pattern)

def get_or_create_spark_session():
    """
    Gets or creates a SparkSession.  This ensures we have a single
    SparkContext across the SDK.
    """
    global __SC__
    if __SC__ is None:
        spark_jars = os.getenv("SDK_JAR_FOLDER")
        __SC__ = SparkSession.builder\
            .config("spark.jars", f"{spark_jars}/postgresql-42.7.3.jar,{spark_jars}/trino-jdbc-469.jar")\
            .appName("DataFoundrySDK")\
            .getOrCreate()
    return __SC__
