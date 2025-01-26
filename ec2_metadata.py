import boto3
import json
import sys
from datetime import datetime

def get_instance_metadata(instance_id=None, key=None):
    
    ec2 = boto3.client('ec2')

    
    if instance_id:
       
        response = ec2.describe_instances(InstanceIds=[instance_id])
    else:
       
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )


    if key:
       
        return extract_key_from_response(response, key)
    

    return json.dumps(response, indent=4, default=json_serial)

def extract_key_from_response(response, key):
    
    try:
        instances = response['Reservations']
        for reservation in instances:
            for instance in reservation['Instances']:
                if key in instance:
                    return json.dumps({key: instance[key]}, indent=4, default=json_serial)
        return json.dumps({"error": "Key not found"}, indent=4, default=json_serial)
    except KeyError as e:
        return json.dumps({"error": str(e)}, indent=4, default=json_serial)

def json_serial(obj):
    
    if isinstance(obj, datetime):
        return obj.isoformat()  
    raise TypeError("Type not serializable")

def main():
    
    instance_id = None
    key = None
    

    if len(sys.argv) > 1:
        instance_id = sys.argv[1]  
        if len(sys.argv) > 2:
            key = sys.argv[2]  
    
    metadata = get_instance_metadata(instance_id, key)

   
    print(metadata)

if __name__ == "__main__":
    main()
