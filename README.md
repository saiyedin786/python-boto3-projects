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
























Auto-Start instance:
