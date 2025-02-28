import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Change region as needed

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0fc82f4dabc05670b',  
    InstanceType='t2.micro',
    KeyName='Linux_Instance_key',  # Change this to your actual key pair name
    SecurityGroupIds=['sg-00aa729c0c3611164'],  # Replace with your security group ID
    SubnetId='subnet-0761682c5f949fe01',  # Replace with your subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'EC2-Linux'}]
        }
    ]
)

