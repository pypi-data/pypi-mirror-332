import pyspark
from pyspark.sql.types import StringType
import os
from pyspark.sql.types import StringType, LongType


def clean_df(df: pyspark.sql.DataFrame):
    df_clean = df.drop("what are your savings objectives?")
    cast_string = []
    for c in df_clean.schema.fields:
        df_clean = df_clean.withColumnRenamed(c.name, c.name.lower())
        if c.dataType == StringType():
            cast_string.append(f"{c.name.lower()} VARCHAR(200)")
    cast_string = ", ".join(cast_string)
    return df_clean, cast_string


class TableBase:
    """
    This database is a palantir database
    """
    table_id = ""
    table_name = "" 
    db_name = ""
    _credential = {
        "host": "trino.ird.vng.vn",
        "port": 443,
        "username": "trino",
        "password": os.environ.get("TRINO_PASSWORD"),
        "catalog_name": "unity",
        "schema_name": "public", # db name 
    } # credential to connect to source

    @classmethod
    def get_db_name(cls):
        return ""

    @classmethod
    def get_table_name(cls):
        return ""

    @classmethod
    def write_spark_jdbc(cls, df: pyspark.sql.dataframe.DataFrame):
        """
        Write dataframe to trino
        Args:
            df (pyspark.sql.dataframe.DataFrame): dataframe
            table_name (str): table name
            mode (str): mode
        Returns:
            bool: True if success, raise error if failed
        """
        mode = "append"
        # mode = "overwrite"
        table_name = cls.get_table_name()
        schema_name = cls.get_db_name()
        try:
            cast_string = []
            for c in df.schema.fields:
                df = df.withColumnRenamed(c.name, c.name.lower())
                if c.dataType == StringType():
                    cast_string.append(f"{c.name.lower()} VARCHAR(200)")
                elif c.dataType == LongType():
                    cast_string.append(f"{c.name.lower()} BIGINT")

            cast_string = ", ".join(cast_string)

            trino_host = "trino.ird.vng.vn"
            trino_port = 8443
            trino_user = "trino"
            trino_password = "gwu8TXB9mbu9mda_nmx"
            trino_catalog = "unity"
            trino_schema = "public"
            jdbc_url = f"jdbc:trino://{trino_host}:{trino_port}/{trino_catalog}/{trino_schema}?user={trino_user}&password={trino_password}"
            if trino_port == 8443:
                jdbc_url += "&SSL=true"

            df.write \
                .format("jdbc") \
                .option("url", jdbc_url) \
                .option("driver", "io.trino.jdbc.TrinoDriver") \
                .option("dbtable", f"{schema_name}.{table_name}") \
                .option("isolationLevel", "NONE") \
                .option("createTableColumnTypes", cast_string) \
                .mode(mode) \
                .save()

        except Exception as e:
            raise e


        print(f'write_spark_jdbc with database: {schema_name} and table_name: {table_name}')
        return True