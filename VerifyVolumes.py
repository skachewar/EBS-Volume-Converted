import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    vid = event['VolumeId']
    try:
        r = ec2.describe_volumes_modifications(VolumeIds=[vid])
        mods = r.get('VolumesModifications', [])
        event['VerifyStatus'] = mods[0]['ModificationState'] if mods else 'Unknown'
    except Exception as e:
        event['VerifyStatus'] = 'Unknown'
        event['VerifyError'] = str(e)
    return event
