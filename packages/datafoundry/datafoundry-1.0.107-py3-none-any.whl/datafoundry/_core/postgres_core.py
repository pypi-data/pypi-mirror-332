# Import the appropriate library here
import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Column, types
from sqlalchemy.engine import reflection
import sqlalchemy
from datafoundry._core.spark_core import get_or_create_spark_session
from datafoundry._core.api_client import ApiClient

class PostgresqlBase:
    """
    PostgresqlBase is a base class for all postgresql databases
    """
    __PG_CREDENTIAL_SET__ = False
    def __init__(self):
        pass

    @classmethod
    def get_uuid(cls) -> str:
        """
        initialize credential for the class
        """
        return ""

    @classmethod
    def set_credential(cls):
        """
        set credential for the class
        """
        if not PostgresqlBase.__PG_CREDENTIAL_SET__:
            api_client = ApiClient(api_domain=os.environ.get("API_SERVER_DOMAIN"), sdk_domain=os.environ.get("SDK_SERVER_DOMAIN"), 
                        auth_domain=os.environ.get("AUTH_SERVER_DOMAIN"))
            token = api_client.get_token(username=os.environ.get("SDK_SERVER_USERNAME"), password=os.environ.get("SDK_SERVER_PASSWORD"))
            uuid = cls.get_uuid()
            pg_credential = api_client.get_source_credential(uuid, token)
            PostgresqlBase.__credential = pg_credential
            PostgresqlBase.__PG_CREDENTIAL_SET__ = True


    

    @classmethod
    def get_connect_sqlalchemy(cls) -> sqlalchemy.engine.Connection:
        """
        return sqlalchemy connection
        """
        # if not PostgresqlBase.__PG_CREDENTIAL_SET__:
        cls.set_credential()
        
        engine = create_engine(
            f"postgresql://{PostgresqlBase.__credential['username']}:{PostgresqlBase.__credential['password']}@{PostgresqlBase.__credential['host']}:{PostgresqlBase.__credential['port']}/{PostgresqlBase.__credential['database_name']}"
        )
        return engine


    @classmethod
    def get_connect_psycopg2(cls, readonly=False) -> psycopg2.extensions.connection:
        """
        return psycopg2 connection
        """
        if not cls.__PG_CREDENTIAL_SET__:
            cls.set_credential()
        
        conn = psycopg2.connect(
            user=PostgresqlBase.__credential['username'],
            password=PostgresqlBase.__credential['password'],
            host=PostgresqlBase.__credential['host'],
            port=PostgresqlBase.__credential['port'],
            database=PostgresqlBase.__credential['database_name']
        )
        if readonly:
            conn.set_session(readonly=readonly)
        return conn


    @classmethod
    def query_pandas(cls, query_string: str=None, table: str = None) -> pd.core.frame.DataFrame:
        """
        return dataframe from query
        Args:
            query_string: str
            table: str
        Returns:
            pd.core.frame.DataFrame
        """
        assert query_string is not None or table is not None, "query_string or table must be provided"


        if not cls.__PG_CREDENTIAL_SET__:
            cls.set_credential()
        engine = cls.get_connect_sqlalchemy()
        if table:
            query_string = f"SELECT * FROM {table}"

        df = pd.read_sql_query(query_string, con=engine)
        return df

    def disconnect(self) -> bool:
        return True   


    @classmethod
    def execute_query(cls, query_string: str):
        """
        execute query and return dataframe
        """
        if not PostgresqlBase.__PG_CREDENTIAL_SET__:
            cls.set_credential()
        conn = cls.get_connect_psycopg2(readonly=False)
        cursor = conn.cursor()
        cursor.execute(query_string)
        conn.commit()
        conn.close()


    @classmethod
    def create_table_from_pandas(cls, df:pd.core.frame.DataFrame, table_name:str, metadata=None, dtype_mapping=None):
        """
        Creates a PostgreSQL table based on a Pandas DataFrame schema and optional metadata.

        Args:
            engine: SQLAlchemy engine connected to the PostgreSQL database.
            df: Pandas DataFrame representing the table structure.
            table_name: Name of the table to create.
            metadata: Optional SQLAlchemy MetaData object to attach the table to.  If None, one is created.
            dtype_mapping: Optional dictionary for custom data type mapping (e.g., {'my_column': types.Text}).
        """
        if not PostgresqlBase.__PG_CREDENTIAL_SET__:
            cls.set_credential()
        engine = cls.get_connect_sqlalchemy()

        if metadata is None:
            metadata = MetaData()

        try:
            inspector = reflection.Inspector.from_engine(engine)
            if table_name in inspector.get_table_names():
                print(f"Table '{table_name}' already exists. Skipping creation.")
                return  # Table already exists

        except Exception as e:
            print(f"Error during table reflection: {e}")
            raise  # Re-raise the exception

        columns = []
        for col_name, data_type in df.dtypes.items():
            sql_type = None

            if pd.api.types.is_integer_dtype(data_type):
                sql_type = types.BigInteger  # Or Integer, SmallInteger, etc.
            elif pd.api.types.is_float_dtype(data_type):
                sql_type = types.Float  # Or Double
            elif pd.api.types.is_bool_dtype(data_type):
                sql_type = types.Boolean
            elif pd.api.types.is_datetime64_any_dtype(data_type):
                sql_type = types.DateTime
            else:
                sql_type = types.String(255)  # Default to String (adjust length as needed)

            if dtype_mapping and col_name in dtype_mapping:
                sql_type = dtype_mapping[col_name]

            if sql_type is None:
                raise ValueError(f"Could not infer SQL type for column '{col_name}'")

            columns.append(Column(col_name, sql_type))

        # Create the Table object
        table = Table(table_name, metadata, *columns)

        # Create the table in the database
        try:
            metadata.create_all(engine)
            print(f"Create table '{table_name}' successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")
            raise
        # insert data into table
        try:
            with engine.connect() as conn:
                conn.execute(table.insert(), df.to_dict(orient="records"))
                conn.commit()
            print(f"Data inserted into table '{table_name}' successfully.")
        except Exception as e:
            print(f"Error inserting data into table: {e}")
        engine.dispose()


    @classmethod
    def query_spark_jdbc(cls, table=None, query=None, schema='public'):
        """
        Creates a Spark DataFrame from a PostgreSQL table or query.
        """
        assert table is not None or query is not None, "table or query must be provided"

        if not cls.__PG_CREDENTIAL_SET__:
            cls.set_credential()

        __SC__ = get_or_create_spark_session()
        jdbc_url = f"jdbc:postgresql://{cls.__credential['host']}:{cls.__credential['port']}/{cls.__credential['database_name']}"
        connection_properties = {
            "user": cls.__credential["username"],
            "password": cls.__credential["password"],
            "driver": "org.postgresql.Driver"
        }

        if query is None:
            sql_stmt = f"SELECT * FROM {schema}.{table}"
        else:
            sql_stmt = query
        df = __SC__.read.jdbc(url=jdbc_url, table=f"({sql_stmt}) as result", properties=connection_properties)

        return df