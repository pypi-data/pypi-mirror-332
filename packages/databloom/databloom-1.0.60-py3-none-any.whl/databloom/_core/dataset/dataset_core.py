import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, types
from sqlalchemy.engine import reflection
from trino.auth import BasicAuthentication
import sqlalchemy
import pyspark
from pyspark.sql.types import StringType, LongType
from databloom._core.spark_core import get_or_create_spark_session
# You can define a customized query class here and an abstract method query().

class DatasetBase:
    """
    DatasetBase is a base class for all trino databases
    """
    def __init__(self):
        self.id = ""
        self.__credential = {
            "host": "",
            "port": "",
            "user": "",
            "password": "",
            "database": "",
            "catalog_name": ""
        }
        self.instance = None

    @staticmethod
    def set_credential(credential: dict):
        """
        set credential for the class
        """
        DatasetBase.__credential = credential


    @staticmethod
    def get_connect_sqlalchemy() -> sqlalchemy.engine.Connection:
        """
        Get sqlalchemy connection
        Args:
            None
        Returns:
            sqlalchemy.engine.Connection: sqlalchemy connection
        """
        user = DatasetBase.__credential["user"]
        password = DatasetBase.__credential["password"]
        host = DatasetBase.__credential["host"]
        port = DatasetBase.__credential["port"]
        database = DatasetBase.__credential["database"]
        engine = create_engine(
            f"trino://{user}:{password}@{host}:{port}/{database}",
            connect_args={
                "auth": BasicAuthentication(user, password),
                "http_scheme": "https",
            }
        )
        return engine

    @staticmethod
    def query_pandas(query_string: str) -> pd.core.frame.DataFrame:
        """
        Query trino and return dataframe
        Args:
            query_string (str): query string
        Returns:
            pd.core.frame.DataFrame: dataframe
        """
        engine = DatasetBase.get_connect_sqlalchemy()
        df = pd.read_sql_query(query_string, engine)
        engine.dispose()
        return df

    @staticmethod
    def execute_query(query_string: str):
        """
        execute query and return dataframe
        """
        engine = DatasetBase.get_connect_sqlalchemy()
        cursor = engine.cursor()
        cursor.execute(query_string)
        engine.commit()
        engine.dispose()
        return True

    @staticmethod
    def create_database(database_name: str):
        """
        create a database
        Args:
            database_name (str): name of the database to create
        """
        DatasetBase.__credential["database"] = database_name
        DatasetBase.instance = DatasetBase.get_connect_sqlalchemy()
        DatasetBase.instance.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        DatasetBase.instance.dispose()
        return True

    @staticmethod
    def create_table_from_pandas(df:pd.core.frame.DataFrame, table_name:str, metadata=None, dtype_mapping=None, schema='public'):
        """
        Creates a PostgreSQL table based on a Pandas DataFrame schema and optional metadata.

        Args:
            engine: SQLAlchemy engine connected to the PostgreSQL database.
            df: Pandas DataFrame representing the table structure.
            table_name: Name of the table to create.
            metadata: Optional SQLAlchemy MetaData object to attach the table to.  If None, one is created.
            dtype_mapping: Optional dictionary for custom data type mapping (e.g., {'my_column': types.Text}).
        """
        engine = DatasetBase.get_connect_sqlalchemy()

        if metadata is None:
            metadata = MetaData(schema=schema)

        # Reflect existing table if it exists, otherwise create a new one
        try:
            inspector = reflection.Inspector.from_engine(engine)
            if table_name in inspector.get_table_names(schema=schema):
                print(f"Table '{table_name}' already exists. Skipping creation.")
                return  # Table already exists

        except Exception as e:
            print(f"Error during table reflection: {e}")
            raise  # Re-raise the exception

        columns = []
        for col_name, data_type in df.dtypes.items():
            sql_type = None

            # Default Pandas dtype to SQLAlchemy type mapping
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

            # Apply custom mapping if provided
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
        
    
    @staticmethod
    def query_spark_jdbc(query_string: str) -> pyspark.sql.dataframe.DataFrame:
        """
        Query trino and return dataframe
        Args:
            query_string (str): query string
            session (pyspark.sql.session.SparkSession): spark session
        Returns:
            pyspark.sql.dataframe.DataFrame: dataframe
        """
        __SC__ = get_or_create_spark_session()
        jdbc_url = f"jdbc:trino://{DatasetBase.__credential['host']}:{DatasetBase.__credential['port']}/{DatasetBase.__credential['catalog_name']}/{DatasetBase.__credential['schema_name']}?user={DatasetBase.__credential['user']}&password={DatasetBase.__credential['password']}"
        if (DatasetBase.__credential['port'] == 8443) or (DatasetBase.__credential['port'] == "8443"):
            jdbc_url = f"jdbc:trino://{DatasetBase.__credential['host']}:{DatasetBase.__credential['port']}/{DatasetBase.__credential['catalog_name']}/{DatasetBase.__credential['schema_name']}?user={DatasetBase.__credential['user']}&password={DatasetBase.__credential['password']}&SSL=true"
        connection_properties = {
            "driver": "io.trino.jdbc.TrinoDriver"
        }
        df_jdbc = __SC__.read.jdbc(url=jdbc_url, table=f"({query_string}) as result", properties=connection_properties)
        return df_jdbc

    @staticmethod
    def write_spark_jdbc(df: pyspark.sql.dataframe.DataFrame, table_name: str, mode: str = "append"):
        """
        Write dataframe to trino
        Args:
            df (pyspark.sql.dataframe.DataFrame): dataframe
            table_name (str): table name
            mode (str): mode
        Returns:
            bool: True if success, raise error if failed
        """
        try:
            cast_string = []
            for c in df.schema.fields:
                df = df.withColumnRenamed(c.name, c.name.lower())
                if c.dataType == StringType():
                    cast_string.append(f"{c.name.lower()} VARCHAR(200)")
                elif c.dataType == LongType():
                    cast_string.append(f"{c.name.lower()} BIGINT")

            cast_string = ", ".join(cast_string)
            jdbc_url = f"jdbc:trino://{DatasetBase.__credential['host']}:{DatasetBase.__credential['port']}/{DatasetBase.__credential['catalog_name']}/{DatasetBase.__credential['schema_name']}?user={DatasetBase.__credential['user']}&password={DatasetBase.__credential['password']}"
            if (DatasetBase.__credential['port'] == 8443) or (DatasetBase.__credential['port'] == "8443"):
                jdbc_url = f"jdbc:trino://{DatasetBase.__credential['host']}:{DatasetBase.__credential['port']}/{DatasetBase.__credential['catalog_name']}/{DatasetBase.__credential['schema_name']}?user={DatasetBase.__credential['user']}&password={DatasetBase.__credential['password']}&SSL=true"
            print(jdbc_url)
            df.write \
                .format("jdbc") \
                .option("url", jdbc_url) \
                .option("driver", "io.trino.jdbc.TrinoDriver") \
                .option("dbtable", table_name) \
                .option("isolationLevel", "NONE") \
                .option("createTableColumnTypes", cast_string) \
                .mode(mode) \
                .save()

        except Exception as e:
            raise e
        return True