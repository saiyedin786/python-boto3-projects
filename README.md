# python-boto3-projects
Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:

1. Setup:
   - Create two EC2 instances.
   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
3. Coding:
   - Using Boto3 in the Lambda function:
     - Detect all EC2 instances with the `Auto-Stop` tag and stop them.
     - Detect all EC2 instances with the `Auto-Start` tag and start them.
4. Testing:
   - Manually invoke the Lambda function.
   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.
Instructions:
1. EC2 Setup:
   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).
   - Tag the first instance with a key `Action` and value `Auto-Stop`.
   - Tag the second instance with a key `Action` and value `Auto-Start`.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

Project solution:
1. EC2 Setup:
   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).
   - Tag the first instance with a key `Action` and value `Auto-Stop`.
   - Tag the second instance with a key `Action` and value `Auto-Start`.

   <img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/bf5d5d1f-ce74-4ee2-a249-254bf18f3fa5" />
   <img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/a0d2bc2a-f248-486d-9138-3496ca6f38f1" />
   <img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5b4ff8a9-9686-44b8-aebb-7f6e99cbf2af" />

Auto-Stop Instance:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/79b9a787-b6f7-41bb-a71c-005b136d2e66" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/a075cbe5-4c46-4c38-9db1-72fdbebd53b7" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/803e2c87-f0e6-450d-90e9-d1ee9ebf20db" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/23196113-98bc-40f1-8d98-3ca7ac8fe89a" />

Now Both instances are up and running:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/b9cbba97-d630-4b3d-9417-d461c0712dd0" />

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)

	Setting up IAM permission to describe,stop and start the EC2 Instances
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d7ae2633-689a-4368-a189-fe133163a1fe" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/e8178d55-409d-4bfa-a792-391ba3b0f613" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/1c77daf5-fe53-44d4-b528-b2ee2e3139a8" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/44d8a84c-2761-42c6-90ca-e29c3872c6b2" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5520d26f-c850-46ff-8d57-a0f7765f8862" />

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/60100fb4-9b84-4039-9203-a062d76ae7ff" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/077d18cd-e2d4-49f3-882d-74601873a5c2" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/e99bbc76-2ba0-4a05-a4d5-1a8024100f51" />

My python script written in my computer
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/0bd10742-78c2-402a-b535-7b5788191ef8" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/945f9d41-c2e8-4d92-bdfb-c24011fa1762" />

Python boto3 code:
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

    


Copying this script to lambda function and deploying into lambada function
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/8f1e719e-be70-4a46-968f-81b6a3af2e8d" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/bea16c90-59b6-4a0a-a13a-a88e0fe9b85f" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/6afa3b0d-56b4-48a6-9059-052ee9108cd4" />

Deploying the lambda function:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/353c298d-6379-4e12-8679-1e9439013f34" />

Now creating the testEvent:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/941c22d3-5739-4c56-962e-2eafadc01db7" />
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

Output on running the lambda function
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/66905650-545e-41f7-bd94-e8596ea1cd7a" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/3e5d85dc-24c2-41a5-9b4c-31992d12daef" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/617cdaa8-5c63-46df-be6b-0d8030f4e79a" />



==================================================================================================================================
Assignment 2
==================================================================================================================================

Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:
1. S3 Setup:
   - Navigate to the S3 dashboard and create a new bucket.
   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.


Project Solution:
1. S3 Setup:
   - Navigate to the S3 dashboard and create a new bucket.
   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/20c9d3ad-65c1-4ede-84db-180179ff0bef" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/81da4a21-c283-4503-92a8-8f995c3f0fd3" />
Created 10 files named abc1 --- abc10 in current date and create 5 files in backdate named def1 ---5 locally in my computer
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/4be97ed5-817a-48b3-b729-efd1a5153aa7" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/a4a74a0f-a0d9-4ccd-825c-6c00e133230e" />

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

Creatinn an IAM Role:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/73eccef6-130b-422c-8d65-69a61013edf9" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/9a9f2080-98d7-4e77-86bc-4f62eb6449b7" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/38b35dbb-989f-41db-8621-cd031cf22dbf" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/1904564c-1e4a-4a63-9f24-1f2290e2983b" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/740d1d92-c4b2-40cb-b818-f3d0a80dea96" />

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/a29cf5c8-708b-4794-adbf-dd9f934a5d28" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/b5801139-a6c6-4d28-be7f-d7ae1b0b5ca4" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/93018285-5431-4484-88a3-111b6d3016a8" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5b21ef8b-7971-42be-a719-f099b17367ac" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/7feb80b0-fcda-4656-9b8c-d21192150e4a" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/9cc15acc-0597-4589-9fe7-f58d6e9696f1" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/68abed15-99cf-429d-b32b-98842bcbab8e" />

Deploying changes:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/b6c04640-f4f5-42c6-b231-82dcbfa28787" />
Creating test event:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/94720831-f19b-4c3a-b70e-8a9b1cfa6b3c" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/95a16aa5-910d-4fd2-9131-67d18b96a308" />


Succcessful  invoking the testEvent
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d925ca2e-a6ed-44ac-bea6-f10bb049a998" />

Vefying from the console:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/bce2943d-cfbb-4c51-86da-0db9b48042ff" />


==============================================================================================================================

Assignment 6: Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS

Objective: Create an automated alerting mechanism for when your AWS billing exceeds a certain threshold.

Task: Set up a Lambda function to check your AWS billing amount daily, and if it exceeds a specified threshold, send an alert via SNS.
Instructions:
1. SNS Setup:
   - Navigate to the SNS dashboard and create a new topic.
   - Subscribe your email to this topic.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach policies that allow reading CloudWatch metrics and sending SNS notifications.
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize boto3 clients for CloudWatch and SNS.
     2. Retrieve the AWS billing metric from CloudWatch.
     3. Compare the billing amount with a threshold (e.g., $50).
     4. If the billing exceeds the threshold, send an SNS notification.
     5. Print messages for logging purposes.
4. Event Source (Bonus):
   - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function daily.
5. Testing:
   - Manually trigger the Lambda function or wait for the scheduled event.
   - If your billing is over the threshold, you should receive an email alert.








Project solution:
SNS Setup (Alert Mechanism)
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/a847b397-c95b-4c28-867d-5ea9434d0d19" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/6a34552d-3bba-4a00-8715-bb4e62c0e38e" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/80a6d463-bd5b-4c83-b002-8c696c58815b" />

Subscribing Email:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/3e952101-8797-49a0-8abe-04f497066af1" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/4be4d28d-76c6-49f7-892a-f51f29da0d4f" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/138b2a8a-9212-4079-95a2-1180d9d9428a" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/b0064ba2-577b-4e0d-9367-42dba0ea741d" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/4205ebd4-74aa-4aa3-8c46-3350b3b05aed" />


Lambda IAM Role Setup:
Creating IAM Role
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/0c98ba13-212c-4258-9eb9-d67f29d335cd" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/097a582f-3a72-4e54-afa6-019d91eb987c" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/ec7bbf5f-b0f2-43a9-b8bc-ab59475211c3" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/b4c71041-7293-45ae-b3be-b6208959ba78" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/44a3d730-64af-49fb-b4c3-34ac81014a27" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/36b4ab01-b9c5-458b-8990-086991320a39" />

Lambda Function Setup:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/dd2b332c-982b-446e-b7dc-70b30a999037" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/69fcce59-d572-4af6-8a92-ab15b9afda9e" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/03b8dc40-22ef-47ac-a0b1-a653d6c9f02b" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/90dd228d-85e7-4cae-9432-ee2c915f5626" />


Boto3-python Code for 
import boto3
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
THRESHOLD = 50.0  # USD
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:254292659362:billing-alert-topic"
# ----------------------------------------

def lambda_handler(event, context):
    # CloudWatch Billing metrics are only in us-east-1
    cloudwatch = boto3.client("cloudwatch", region_name="us-east-1")
    sns = boto3.client("sns")

    # Time range (last 1 day)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    # Get billing metric
    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/Billing",
        MetricName="EstimatedCharges",
        Dimensions=[
            {
                "Name": "Currency",
                "Value": "USD"
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=["Maximum"]
    )

    if not response["Datapoints"]:
        print("No billing data available")
        return

    billing_amount = response["Datapoints"][0]["Maximum"]
    print(f"Current estimated billing: ${billing_amount}")

    # Compare with threshold
    if billing_amount > THRESHOLD:
        message = (
            f"AWS Billing Alert!\n\n"
            f"Current estimated charges: ${billing_amount}\n"
            f"Threshold: ${THRESHOLD}\n"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Billing Alert",
            Message=message
        )

        print("Alert sent via SNS")
    else:
        print("Billing is within limit")


<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/64a27acd-fe2d-43d6-87ec-636247283d6d" />

Creating a test event
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/78f100b6-8988-4a32-8a2c-29cbbfc49c5e" />


Testing with testEvent
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5037b30c-b3bf-4561-adfd-80335d3ef8de" />

Create EventBridge Rule:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d01fc044-e77e-48f8-bdc5-c65df254e1e5" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/31137572-4b0e-4e1d-a950-3cc5cd99b1ea" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/2f671360-d544-4c72-97ee-b4c2818e82df" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/f6ab6405-ba50-450d-9b85-d73c52c0a1c7" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/eb77de69-2cd0-4732-b8e3-57b9e183043d" />
Triggering manually the lambda function:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/783f1eda-c5e0-40a0-a7c2-e1eac5ffd425" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/2f0d8cb4-657a-49b4-aebe-dbc4e400b088" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/4a40c1bf-1119-474f-8e25-9bd9a611667c" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/95dad4b1-97c9-4e5a-9aa3-51f7114e03b8" />




==========================================================================================================================================

Assignment 7: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS

Objective: Automate the process to receive an alert whenever an item in a DynamoDB table gets updated.
Task: Set up a Lambda function that gets triggered when an item in a DynamoDB table is updated and sends an alert via SNS.
Instructions:
1. DynamoDB Setup:
   - Navigate to the DynamoDB dashboard and create a table.
   - Add a few items to the table.
2. SNS Setup:
   - Navigate to the SNS dashboard and create a new topic.
   - Subscribe your email to this topic.
3. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach policies that allow Lambda to read DynamoDB Streams and send SNS notifications.
4. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Extract the modified DynamoDB item from the event.
     2. Send an SNS notification detailing the change.
     3. Log messages for tracking.
5. DynamoDB Stream:
   - Enable DynamoDB Streams on your table and set the view type to "New and old images".
   - Attach the Lambda function to the DynamoDB Stream.
6. Testing:
   - Update an item in your DynamoDB table.
   - Confirm that you receive an SNS alert detailing the change.
Submission:
- Provide the Python code used in the Lambda function.
- Document the steps followed.
- Share screenshots of the SNS alert and Lambda logs.




Project solution:
DynamoDB Setup:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/ac506db2-f619-4fed-9ed9-5471c2ed082b" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/e4703b10-b094-4872-a14c-e9500c7d534b" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/69fac9ac-6b3a-4822-a3f8-b15d5e976da1" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/70ef94ae-01c0-468b-b3dc-085d2d2fb7f7" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/2eef2253-f1fd-472d-83fd-0332160a6674" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/add9cbac-d76e-4eb0-9f03-d9ebdc39c405" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/3b46c35f-748d-4afc-bcd3-44fad6b6b498" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/3f61c7b0-e354-43a2-a90f-bfa541331cb6" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/7c61770c-99c8-43cb-ba60-21e2bb391368" />


SNS Setup:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/294d7a63-27a0-4103-a713-774b9d41100b" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/4af5b057-6c1a-417e-8534-371fb465b2cb" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d1c23b5a-0593-472b-a377-0e3339fb9cab" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/097d5116-9f2b-4bb8-834a-cd40533e9bf7" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/6ecba0b1-170c-415d-89a6-fef3dd78df92" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/0dbe63f4-56bf-4fe1-962b-fd813ba6a310" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/65ac968a-27c5-462c-8de6-678d1390f3d8" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/015d83b4-1e6f-437a-a1fd-c5cb9e6a7a07" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/3870a299-51f6-4f73-a07d-c55ceeb31eaa" />

IAM Role for Lambda:
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5be86522-b8ec-4a6d-8caa-bfc59c4c5d21" />
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/f5a83429-fdf4-4ab5-a45c-7f0385c74017" />

























































































