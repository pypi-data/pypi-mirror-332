from src.core_pro import AWS
from pathlib import Path
from rich import print


# config
bucket_name = 'sg-vnbi-ops-hive'
s3 = AWS(bucket_name)

# check file
prefix = "dev_vnbi_ops/ds_cx__item_marketplace_listening__s3_adhoc"
files = s3.get_all_files(prefix=prefix)
files = [i for i in files if "parquet" not in i]
print(files)

# delete
# for f in files:
#     s3.delete_file(f)

# upload
# path = Path("/media/kevin/data_4t/cx/product_review/deploy/inference/2025-03-05/export_s3")
# files = [*path.glob("*.parquet")]
# print(len(files))
#
# for f in files:
#     s3.upload_file(f, prefix)
