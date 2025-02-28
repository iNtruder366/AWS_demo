import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.create_instances(
    ImageId='ami-0fc82f4dabc05670b',
    InstanceType='t2.micro',
    KeyName='Linux_Instance_key',
    SecurityGroupIds=['sg-00aa729c0c3611164'],
    SubnetId='subnet-0761682c5f949fe01',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'EC2_Linux'}]
        }
    ]
)
