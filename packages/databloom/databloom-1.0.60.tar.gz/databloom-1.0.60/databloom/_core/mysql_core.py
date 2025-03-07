# Import the appropriate library here
import sqlalchemy
from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, types
from sqlalchemy.engine import reflection
from databloom._core.spark_core import get_or_create_spark_session
# You can define a customized query class here and an abstract method query().

class MysqlBase:
    """
    MysqlBase is a base class for all mysql databases
    """
    def __init__(self):
        self.id = ""
        self.__credential = {
            "host": "",
            "port": "",
            "username": "",
            "password": "",
            "database_name": ""
        }
        self.instance = None

    def get_instance(self):
        """
        create a singleton instance of the class
        """
        self.instance = MysqlBase.get_connect_mysql()
        return self.instance

    @staticmethod
    def set_credential(credential: dict):
        """
        set credential for the class
        """
        MysqlBase.__credential = credential

    @staticmethod
    def get_connect_sqlalchemy() -> sqlalchemy.engine.Connection:
        """
        return sqlalchemy connection
        """
        engine = create_engine(
            f"mysql://{MysqlBase.__credential['username']}:{MysqlBase.__credential['password']}@{MysqlBase.__credential['host']}:{MysqlBase.__credential['port']}/{MysqlBase.__credential['database_name']}"
        )
        return engine

    @staticmethod
    def get_connect_mysql() -> mysql.connector.connection.MySQLConnection:
        """
        return customize query class
        """
        return mysql.connector.connect(
            host=MysqlBase.__credential['host'],
            user=MysqlBase.__credential['username'],
            password=MysqlBase.__credential['password'],
            database=MysqlBase.__credential['database_name']
        )

    @staticmethod
    def query_pandas(query_string: str) -> pd.core.frame.DataFrame:
        """
        return dataframe from query
        """
        engine = MysqlBase.get_connect_sqlalchemy()
        df = pd.read_sql_query(query_string, con=engine)
        engine.dispose()
        return df


    @staticmethod
    def create_table_from_pandas(df:pd.core.frame.DataFrame, table_name:str, metadata=None, dtype_mapping=None):
        """
        Creates a PostgreSQL table based on a Pandas DataFrame schema and optional metadata.

        Args:
            engine: SQLAlchemy engine connected to the PostgreSQL database.
            df: Pandas DataFrame representing the table structure.
            table_name: Name of the table to create.
            metadata: Optional SQLAlchemy MetaData object to attach the table to.  If None, one is created.
            dtype_mapping: Optional dictionary for custom data type mapping (e.g., {'my_column': types.Text}).
        """
        engine = MysqlBase.get_connect_sqlalchemy()

        if metadata is None:
            metadata = MetaData()

        # Reflect existing table if it exists, otherwise create a new one
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
    def query_spark_df(table=None, query=None):
        """
        Creates a Spark DataFrame from a PostgreSQL table or query.
        """
        __SC__ = get_or_create_spark_session()

        # Define JDBC URL
        jdbc_url = f"jdbc:mysql://{MysqlBase.__credential['host']}:{MysqlBase.__credential['port']}/{MysqlBase.__credential['database_name']}"
        # Define connection properties
        connection_properties = {
            "user": MysqlBase.__credential["username"],
            "password": MysqlBase.__credential["password"],
            "driver": "com.mysql.cj.jdbc.Driver"
        }

        if query is None:
            sql_stmt = f"SELECT * FROM {table}"
        else:
            sql_stmt = query
        # Read data from PostgreSQL
        df = __SC__.read.jdbc(url=jdbc_url, table=f"({sql_stmt}) as result", properties=connection_properties)
        return df