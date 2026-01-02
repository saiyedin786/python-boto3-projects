import json
import boto3

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    

    auto_stop_instances = []
    auto_start_instances = []

    # 2. Describe instances with Auto-Stop and Auto-Start tags
    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Action",
                "Values": ["Auto-Stop", "Auto-Start"]
            },
            {
                "Name": "instance-state-name",
                "Values": ["running", "stopped"]
            }
        ]
    )

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            # print(instance)
            # print(instance["Tags"])
            if 'Tags' in instance:
                
                for tag in instance['Tags']:
                    if tag['Key'] == 'Action' and tag['Value']=="Auto-Stop":
                        auto_stop_instances.append(instance_id)
                        print(auto_stop_instances)
                    
                    if tag['Key'] == 'Action' and tag['Value']=="Auto-Start":
                        auto_start_instances.append(instance_id)
                        print(auto_start_instances)

    # 3. Stop Auto-Stop instances
    if auto_stop_instances:
        ec2.stop_instances(InstanceIds=auto_stop_instances)
        print("Stopped instances:")
        for i in auto_stop_instances:
            print(f"  - {i}")

    # 3. Start Auto-Start instances
    if auto_start_instances:
        ec2.start_instances(InstanceIds=auto_start_instances)
        print("Started instances:")
        for i in auto_start_instances:
            print(f"  - {i}")

    # 4. Logging if no instances matched
    if not auto_stop_instances and not auto_start_instances:
        print("No instances were affected.")


    
