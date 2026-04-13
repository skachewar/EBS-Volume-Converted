import boto3

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:ap-southeast-2:735189764173:EBS-Conversion-Alerts'

def lambda_handler(event, context):
    msg = f'''EBS Volume Automation Result\n\nVolume ID: {event.get('VolumeId', 'Unknown')}\nInstance ID: {event.get('InstanceId', 'Unknown')}\nStatus: {event.get('Status', 'Unknown')}\nVerify: {event.get('VerifyStatus', 'Unknown')}\nError Code: {event.get('ErrorCode', '')}\nError Message: {event.get('ErrorMessage', '')}'''
    sns.publish(TopicArn=TOPIC_ARN, Subject='EBS Volume Converted', Message=msg)
    return {'message': 'SNS Sent'}
