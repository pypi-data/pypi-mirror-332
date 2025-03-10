import os
import pyspark
from pyspark.sql.types import StringType, LongType, FloatType, DateType, BooleanType, TimestampType
from pyspark.sql import functions as F
from datafoundry._core.spark_core import get_or_create_spark_session
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

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

    @classmethod
    def get_db_name(cls):
        return ""

    @classmethod
    def get_table_name(cls):
        return ""

    @classmethod
    def get_connect_sqlalchemy(cls) -> sqlalchemy.engine.Connection:
        """
        return sqlalchemy connection
        """
        trino_host = os.environ.get("TRINO_HOST")
        trino_port = os.environ.get("TRINO_PORT")
        trino_user = os.environ.get("TRINO_USER")
        trino_password = os.environ.get("TRINO_PASSWORD")
        trino_catalog = os.environ.get("TRINO_CATALOG")
        schema_name = cls.get_db_name()
        engine = create_engine(
            f"trino://{trino_user}:{trino_password}@{trino_host}:{trino_port}/{trino_catalog}/{schema_name}"
        )
        return engine

    @classmethod
    def query_pandas(cls) -> pd.core.frame.DataFrame:
        """
        return pandas dataframe
        """
        engine = cls.get_connect_sqlalchemy()
        
        table_name = cls.get_table_name()
        # TODO: get schema name
        # schema_name = cls.get_db_name()

        df = pd.read_sql_table(table_name, engine)
        return df

    @classmethod
    def query_jdbc(cls):
        """
        Read dataframe from trino
        Returns:
            pyspark.sql.dataframe.DataFrame: dataframe
        """
        table_name = cls.get_table_name()
        schema_name = cls.get_db_name()
        trino_host = os.environ.get("TRINO_HOST")
        trino_port = os.environ.get("TRINO_PORT")
        trino_user = os.environ.get("TRINO_USER")
        trino_password = os.environ.get("TRINO_PASSWORD")
        trino_catalog = os.environ.get("TRINO_CATALOG")
        jdbc_url = f"jdbc:trino://{trino_host}:{trino_port}/{trino_catalog}/{schema_name}?user={trino_user}&password={trino_password}"

        if (trino_port == 8443) or (trino_port == '8443'):
            jdbc_url += "&SSL=true"

        __SC__ = get_or_create_spark_session()
        df = __SC__.read.format("jdbc") \
                .option("url", jdbc_url) \
                .option("driver", "io.trino.jdbc.TrinoDriver") \
                .option("isolationLevel", "NONE") \
                .option("dbtable", f"{schema_name}.{table_name}") \
                .load()
        return df


    @classmethod
    def write_jdbc(cls, df: pyspark.sql.dataframe.DataFrame, limit: int = 30):
        """
        Write dataframe to trino
        Args:
            df (pyspark.sql.dataframe.DataFrame): dataframe
            table_name (str): table name
            mode (str): mode
        Returns:
            bool: True if success, raise error if failed
        """
        # mode = "overwrite"
        mode = "append"
        table_name = cls.get_table_name()
        schema_name = cls.get_db_name()
        try:
            cast_string = []
            for c in df.schema.fields:
                if c.dataType == BooleanType():
                    df = df.withColumn(c.name, F.when(F.col(c.name) == 'TRUE', 1).otherwise(0))
                elif c.dataType == StringType():
                    cast_string.append(f"{c.name.lower()} VARCHAR(200)")
                elif c.dataType == LongType():
                    df = df.withColumn(c.name, (df[c.name].cast('integer')/1000).cast('integer'))
                    cast_string.append(f"{c.name.lower()} BIGINT")
                elif c.dataType == FloatType():
                    cast_string.append(f"{c.name.lower()} FLOAT")
                elif c.dataType == DateType():
                    cast_string.append(f"{c.name.lower()} DATE")
                elif c.dataType == TimestampType():
                    cast_string.append(f"{c.name.lower()} TIMESTAMP")
                else:
                    print(f"type {c.dataType} not supported")


            cast_string = ", ".join(cast_string)

            trino_host = os.environ.get("TRINO_HOST")
            trino_port = os.environ.get("TRINO_PORT")
            trino_user = os.environ.get("TRINO_USER")
            trino_password = os.environ.get("TRINO_PASSWORD")
            trino_catalog = os.environ.get("TRINO_CATALOG")
            jdbc_url = f"jdbc:trino://{trino_host}:{trino_port}/{trino_catalog}/{schema_name}?user={trino_user}&password={trino_password}"
            if (trino_port == 8443) or (trino_port == '8443'):
                jdbc_url += "&SSL=true"

            df.limit(limit).write \
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


    # def write_jdbc_pg(cls, df: pyspark.sql.dataframe.DataFrame):
    @classmethod
    def write_jdbc_pg(cls, df: pyspark.sql.dataframe.DataFrame, mode: str = "append"):
        """
        Write dataframe to trino
        Args:
            df (pyspark.sql.dataframe.DataFrame): dataframe
            table_name (str): table name
            mode (str): mode
        Returns:
            bool: True if success, raise error if failed
        """
        # mode = "overwrite"
        # mode = "append"
        table_name = cls.get_table_name()
        schema_name = cls.get_db_name()
        try:
            cast_string = []
            for c in df.schema.fields:
                df = df.withColumnRenamed(c.name, c.name.lower())
                if c.dataType == BooleanType():
                    df = df.withColumn(c.name, F.when(F.col(c.name) == 'TRUE', 1).otherwise(0))
                elif c.dataType == TimestampType():
                    df = df.withColumn(c.name, F.to_date(c.name))
                elif c.dataType == StringType():
                    cast_string.append(f"{c.name.lower()} VARCHAR(200)")
                elif c.dataType == LongType():
                    cast_string.append(f"{c.name.lower()} BIGINT")
                elif c.dataType == FloatType():
                    cast_string.append(f"{c.name.lower()} FLOAT")
                elif c.dataType == DateType():
                    cast_string.append(f"{c.name.lower()} DATE")
                else:
                    print(f"column {c.name} type {c.dataType} not supported")

            cast_string = ", ".join(cast_string)
            postgres_host = os.environ.get("POSTGRES_HOST")
            postgres_port = os.environ.get("POSTGRES_PORT")
            postgres_database = os.environ.get("POSTGRES_DATABASE")
            postgres_username = os.environ.get("POSTGRES_USERNAME")
            postgres_password = os.environ.get("POSTGRES_PASSWORD")

            # JDBC URL for PostgreSQL
            jdbc_url = f"jdbc:postgresql://{postgres_host}:{postgres_port}/{postgres_database}"

            # Properties for the connection
            connection_properties = {
                "user": postgres_username,
                "password": postgres_password,
                "driver": "org.postgresql.Driver"
            }
            # Write DataFrame to PostgreSQL
            df.write \
                .jdbc(url=jdbc_url, table=f"{schema_name}.{table_name}", mode=mode, properties=connection_properties)

        except Exception as e:
            raise e

        print(f'write_spark_jdbc with database: {schema_name} and table_name: {table_name}')
        return True