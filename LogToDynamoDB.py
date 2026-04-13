import boto3
from datetime import datetime

table = boto3.resource('dynamodb').Table('EBS-Conversion-Logs')

def lambda_handler(event, context):
    item = {
        'VolumeId': event['VolumeId'],
        'Timestamp': datetime.utcnow().isoformat(),
        'InstanceId': event.get('InstanceId', 'NA'),
        'OldType': 'gp2',
        'NewType': 'gp3',
        'Status': event.get('Status', 'Unknown'),
        'VerifyStatus': event.get('VerifyStatus', 'Unknown'),
        'ErrorCode': event.get('ErrorCode', ''),
        'ErrorMessage': event.get('ErrorMessage', '')
    }
    table.put_item(Item=item)
    return event
