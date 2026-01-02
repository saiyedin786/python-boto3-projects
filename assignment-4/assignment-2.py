import boto3
from datetime import datetime, timezone, timedelta

# ---------------------------
# Configuration
# ---------------------------
REGION = "ap-south-1"            # Change if needed
VOLUME_ID = "vol-0ca1509943ecd7e56"  # Replace with your EBS Volume ID
RETENTION_DAYS = 2

# ---------------------------
# Initialize EC2 client
# ---------------------------
ec2 = boto3.client("ec2", region_name=REGION)

# ---------------------------
# Create Snapshot
# ---------------------------
response = ec2.create_snapshot(
    VolumeId=VOLUME_ID,
    Description=f"Automated snapshot for {VOLUME_ID}"
)
print(response["SnapshotId"])

snapshot_id = response["SnapshotId"]
print(f"Created snapshot: {snapshot_id}")

# ---------------------------
# Find & Delete Old Snapshots
# ---------------------------
cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

deleted_snapshots = []

snapshots = ec2.describe_snapshots(OwnerIds=["self"])["Snapshots"]

for snapshot in snapshots:
    start_time = snapshot["StartTime"]
    snap_id = snapshot["SnapshotId"]

    if start_time < cutoff_date:
        ec2.delete_snapshot(SnapshotId=snap_id)
        deleted_snapshots.append(snap_id)
        print(f"🗑️ Deleted snapshot: {snap_id}")

# ---------------------------
# Summary Logs
# ---------------------------
print("\n===== Snapshot Summary =====")
print(f"Created Snapshot ID: {snapshot_id}")

if deleted_snapshots:
    print("Deleted Snapshot IDs:")
    for sid in deleted_snapshots:
        print(f" - {sid}")
else:
    print("No snapshots were deleted.")
