import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    vid = event['VolumeId']
    try:
        vol = ec2.describe_volumes(VolumeIds=[vid])['Volumes'][0]
        if vol['VolumeType'] == 'gp3':
            event['Status'] = 'AlreadyConverted'
            return event
        ec2.modify_volume(VolumeId=vid, VolumeType='gp3')
        event['Status'] = 'ModificationStarted'
    except ClientError as e:
        event['Status'] = 'Failed'
        event['ErrorCode'] = e.response['Error']['Code']
        event['ErrorMessage'] = e.response['Error']['Message']
    return event
