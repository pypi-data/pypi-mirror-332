import boto3
import os
from pathlib import Path
from tqdm import tqdm
from google.cloud import storage
import datetime
import polars as pl
import json
from rich import print


def polars_to_presto_type(pl_dtype):
    mapping = {
        pl.Int8: "tinyint",
        pl.Int16: "smallint",
        pl.Int32: "integer",
        pl.Int64: "bigint",
        pl.Float32: "real",
        pl.Float64: "double",
        pl.Decimal: "decimal",
        pl.Utf8: "varchar",
        pl.Binary: "varbinary",
        pl.Date: "date",
        pl.Time: "time",
        pl.Datetime: "timestamp",
        pl.Boolean: "boolean",
        pl.List: "array",
        pl.Struct: "map",
    }
    return mapping.get(pl_dtype, "varchar")


def polars_to_flink_type(pl_dtype):
    mapping = {
        pl.Int8: "TINYINT",
        pl.Int16: "SMALLINT",
        pl.Int32: "INTEGER",
        pl.Int64: "BIGINT",
        pl.UInt8: "SMALLINT",
        pl.UInt16: "INTEGER",
        pl.UInt32: "BIGINT",
        pl.UInt64: "BIGINT",
        pl.Float32: "FLOAT",
        pl.Float64: "DOUBLE",
        pl.Boolean: "BOOLEAN",
        pl.Utf8: "VARCHAR",
        pl.Date: "DATE",
        pl.Datetime: "TIMESTAMP",
        pl.Duration: "INTERVAL DAY TO SECOND",
        pl.Categorical: "VARCHAR",
    }
    return mapping.get(pl_dtype, "STRING")


class AWS:
    def __init__(self, bucket_name: str):
        dict_ = {
            "endpoint_url": os.environ["AWS_ENDPOINT_URL"],
            "aws_access_key_id": os.environ["PRESTO_USER"],
            "aws_secret_access_key": os.environ["PRESTO_PASSWORD"],
        }
        self.bucket_name = bucket_name
        self.client = boto3.client("s3", **dict_)
        self.my_bucket = boto3.resource("s3", **dict_).Bucket(self.bucket_name)
        self.status = f"[green3]🐸 S3:[/]"

    def get_all_files(self, prefix: str) -> list:
        paginator = self.client.get_paginator('list_objects_v2')
        files = []
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
            if 'Contents' in page:
                files.extend(obj['Key'] for obj in page['Contents'])
        return files

    def delete_file(self, key: str):
        self.client.delete_object(Bucket=self.bucket_name, Key=key)
        print(f"{self.status} [Remove]: {key}")

    def empty_trash(self):
        lst_trash = [i for i in self.my_bucket.objects.all() if ".Trash" in i.key]
        for i in lst_trash:
            i.delete()
        print(f"{self.status} [Empty Trash]: {len(lst_trash)} files")

    def get_file_size(self, key: str):
        return self.my_bucket.Object(key).content_length

    def upload_file(self, file: Path, folder: str = None):
        file_size = file.stat().st_size
        desc = f"[Upload] {file.name}, size: {file_size / 1024**2:,.2f}MB"
        s3_key = f"{folder}/{file.name}" if folder else file.name
        with tqdm(total=file_size, unit="B", unit_scale=True, desc=desc) as pbar:
            self.my_bucket.upload_file(
                file,
                Key=s3_key,
                Callback=lambda x: pbar.update(x),
                ExtraArgs={'ContentType': 'application/octet-stream'}
            )

        # Verify the upload
        response = self.client.head_object(Bucket=self.bucket_name, Key=s3_key)
        print(f"Upload successful. ETag: {response.get('ETag')}")
        return True

    def download_file(self, path: Path, key: str):
        file_size = self.get_file_size(key)
        desc = f"[Download] {key}, size: {file_size / 1024**2:,.2f}MB"
        with tqdm(total=file_size, unit="B", unit_scale=True, desc=desc) as pbar:
            self.my_bucket.download_file(
                Key=key,
                Filename=path / key.split("/")[-1],
                Callback=lambda x: pbar.update(x),
            )

    def create_presigned_url(self, key: str, expiration: int = 900):
        url = self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket_name, "Key": key},
            ExpiresIn=expiration,
        )
        print(f"{self.status} [Pre-signed] {key} in {expiration / 3600}h")
        return url

    def convert_dataframe_flink_config(
        self,
        df: pl.DataFrame,
        key: str,
        table_name: str,
        file_type: str = "parquet",
    ):
        polars_schema = dict(df.schema)

        # convert to flink config
        flink_schema = {
            field: polars_to_flink_type(dtype) for field, dtype in polars_schema.items()
        }
        lines = []
        for i, (k, v) in enumerate(flink_schema.items()):
            if i == 0:
                lines.append(f"{k}:{v}")
            else:
                lines.append(f", {k}: {v}")
        flink_schema = "{\n" + "\n".join(lines) + "\n}"

        # convert to sql script
        sql_schema = [
            f"{field} {polars_to_presto_type(dtype)}"
            for field, dtype in polars_schema.items()
        ]
        sql_schema = "\n\t, ".join(sql_schema)

        flink_config = f"""
env {{
}}      

source {{
    S3FileSource {{
        datasource_name = "my_s3"
        path = "s3a://{self.bucket_name}/{key}"
        format = "{file_type}"
        schema = {flink_schema}
        endpoint = "{os.environ["AWS_ENDPOINT_URL"]}"
        bucket = "{self.bucket_name}"
        # ignore-parse-errors = "true"
        # skip-first-data-row = "true"
        result_table_name = "s3FileSource"
        access_key = "{{$.HADOOP_USER_NAME}}"
        secret_key = "{{$.HADOOP_USER_RPCPASSWORD}}"
        endpoint = "https://s3g.data-infra.shopee.io"
      }}
}}

transform {{
  Sql {{
    sql = "select * from `s3FileSource`"
    result_table_name = "transformed"
  }}
}}
  
sink {{
  HiveSink {{
    source_table_name = "transformed"
    result_table_name = "hive.{table_name}"
  }}
}}
        """

        sql_create_table = f"""
CREATE TABLE {table_name} (
    {sql_schema}
)
        """
        return flink_config, sql_create_table


class Gcloud:
    def __init__(self, json_path: str):
        self.client = storage.Client.from_service_account_json(str(json_path))
        self.status = f"[green3]🐻‍❄️ Gcloud:[/]"
        self.bucket_name = "kevin-bi"
        self.bucket = self.client.bucket(self.bucket_name)

    def download_file(self, blob_path: str, file_path: Path):
        blob = self.bucket.blob(blob_path)
        blob.download_to_filename(file_path)
        print(f"{self.status} download {blob_path}")

    def upload_file(self, blob_path: str, file_path: Path):
        blob_path_full = f"{blob_path}/{file_path.name}"
        blob = self.bucket.blob(blob_path_full)
        blob.upload_from_filename(file_path)
        print(f"{self.status} upload {file_path.stem} to {blob_path}")
        return blob_path_full

    def generate_download_signed_url_v4(self, blob_file, minutes=15):
        blob = self.bucket.blob(blob_file)
        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(minutes=minutes),
            method="GET",
        )
        print(f"{self.status} Presigned [{blob_file}] in {minutes} mins \nUrl: {url}")
        return url
