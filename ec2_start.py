import boto3
region = 'ap-south-1'
instances = [] # Provide Instace ID's to be scheduled

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    
    client = boto3.client('sns')
    response = client.publish(
        TopicArn='arn:aws:sns:ap-south-1:309468567045:mySlackNotifications', # Create the ARN for Push Notification Link - https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html
        Message='All the EC2 instances that are scheduled by AWS Lambda have been started', # Custom Messages
        Subject='LeanApps AWS servers have been started' # Custom Subject
    )