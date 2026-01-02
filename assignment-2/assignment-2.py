import boto3
from datetime import datetime, timezone, timedelta


# ---------- CONFIG ----------
BUCKET_NAME = "ismailsaiyed-demo-bucket"
DAYS_OLD = 3
# ----------------------------

# 1. Initialize S3 client
s3 = boto3.client("s3")

# Calculate cutoff date
cutoff_date = datetime.now(timezone.utc) - timedelta(days=DAYS_OLD)
print("cutoff date -" , cutoff_date)

# 2. List objects in the bucket
paginator = s3.get_paginator("list_objects_v2")

for page in paginator.paginate(Bucket=BUCKET_NAME):
    for obj in page["Contents"]:
        print(obj["Key"])
        print(obj["LastModified"])


objects_to_delete = []
deleted_keys = []

for page in paginator.paginate(Bucket=BUCKET_NAME):
  
    if "Contents" not in page:
        continue

    for obj in page["Contents"]:
        last_modified = obj["LastModified"]
        print("last modified ---",last_modified)

        # 3. Check if object is older than 3 days
        if last_modified < cutoff_date:
            objects_to_delete.append({"Key": obj["Key"]})
            deleted_keys.append(obj["Key"])


# Delete old objects (batch delete: max 1000 at a time)
if objects_to_delete:
    for i in range(0, len(objects_to_delete), 1000):
        batch = objects_to_delete[i:i + 1000]
        response = s3.delete_objects(
            Bucket=BUCKET_NAME,
            Delete={"Objects": batch}
        )
        print(f"Deleted {len(batch)} objects")
    for key in deleted_keys:
            print("deleted",key)
else:
    print("No objects older than 3 days found.")

  