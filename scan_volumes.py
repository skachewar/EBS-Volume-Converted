import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    resp = ec2.describe_volumes(Filters=[
        {'Name': 'volume-type', 'Values': ['gp2']},
        {'Name': 'tag:AutoConvert', 'Values': ['true']}
    ])
    result = []
    for v in resp['Volumes']:
        result.append({
            'VolumeId': v['VolumeId'],
            'InstanceId': v['Attachments'][0]['InstanceId'] if v.get('Attachments') else 'NotAttached',
            'Size': v['Size'],
            'AZ': v['AvailabilityZone'],
            'OldType': 'gp2'
        })
    return result
