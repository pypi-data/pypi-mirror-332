import logging
import os
import uuid

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from airflow.models import BaseOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.decorators import apply_defaults


class SqlToS3ParquetOperator(BaseOperator):
    """
    Custom Airflow Operator to extract data from PostgreSQL, convert it to Parquet format, and upload to S3.
    """

    template_fields = (
        "query",
        "s3_key",
        "table_name",
        "table_schema",
    )

    data_converter = {
        "uuid": pa.string(),
        "character varying": pa.string(),
        "numeric": pa.decimal128(36, 18),
        "integer": pa.int64(),
        "bigint": pa.int64(),
        "timestamp without time zone": pa.timestamp("ms"),
        "boolean": pa.bool_(),
        "jsonb": pa.string(),
        "json": pa.string(),
        "inet": pa.string(),
        "ARRAY": pa.string(),
        "text": pa.string(),
        "date": pa.date32(),
        "double precision": pa.float64(),
        "timestamp with time zone": pa.timestamp("ms"),
        "smallint": pa.int16(),
        "USER-DEFINED": pa.string(),
    }

    @apply_defaults
    def __init__(
        self,
        query: str,
        s3_bucket: str,
        s3_key: str,
        sql_conn_id: str,
        aws_conn_id: str,
        table_schema: str,
        table_name: str,
        parquet_version: str = "1.0",
        replace: bool = True,
        *args,
        **kwargs,
    ):
        super(SqlToS3ParquetOperator, self).__init__(*args, **kwargs)
        self.query = query
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.sql_conn_id = sql_conn_id
        self.aws_conn_id = aws_conn_id
        self.table_schema = table_schema
        self.table_name = table_name
        self.parquet_version = parquet_version
        self.replace = replace

    def get_pg_schema(self, cursor):
        """
        Retrieve the column names and data types from the PostgreSQL information schema.
        """
        cursor.execute(
            f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = '{self.table_schema}'
            AND table_name = '{self.table_name}';
        """
        )
        return cursor.fetchall()

    def map_pg_to_pa(self, pg_schema):
        """
        Map PostgreSQL schema to PyArrow schema.
        """
        fields = []
        for column_name, data_type in pg_schema:
            pa_type = self.data_converter.get(data_type, pa.string())  # Default to string() if type is not found
            fields.append((column_name, pa_type))
        return pa.schema(fields)

    def execute(self, context):
        """
        Execute the data extraction, conversion, and upload process.
        """
        # Render the query with actual dates
        rendered_query = self.render_template(self.query, context)

        # Extract data from SQL database for schema information
        pg_hook = PostgresHook(postgres_conn_id=self.sql_conn_id)
        connection = pg_hook.get_conn()
        cursor = connection.cursor()

        try:
            # Get PostgreSQL schema
            pg_schema = self.get_pg_schema(cursor)
            logging.info(f"PostgreSQL schema: {pg_schema}")

            # Map PostgreSQL schema to PyArrow schema
            parquet_schema = self.map_pg_to_pa(pg_schema)
            logging.info(f"Parquet schema: {parquet_schema}")

            # Execute data extraction query
            cursor.execute(rendered_query)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=columns)

            # Generate a unique file path
            unique_id = uuid.uuid4()
            local_parquet_file = f"/tmp/postgres_data_{unique_id}.parquet"

            # Write DataFrame to a Parquet file with generated schema and version
            table = pa.Table.from_pandas(df, schema=parquet_schema)
            pq.write_table(table, local_parquet_file, version=self.parquet_version)

            # Upload to S3
            s3_hook = S3Hook(aws_conn_id=self.aws_conn_id)
            logging.info(f"Uploading to S3 bucket: {self.s3_bucket}, key: {self.s3_key}, replace: {self.replace}")
            s3_hook.load_file(
                filename=local_parquet_file, key=self.s3_key, bucket_name=self.s3_bucket, replace=self.replace
            )

            # Clean up local file
            os.remove(local_parquet_file)
            logging.info(f"Data written to {self.s3_bucket}/{self.s3_key} with Parquet version {self.parquet_version}")

        except Exception as e:
            logging.error(f"Error during execution: {e}")
            raise

        finally:
            cursor.close()
            connection.close()