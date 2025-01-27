# AWSMetaData
Retrieve AWS meta data of the active instances
Step by step guide to run the python program locally

Step 1: Install python
Step 2: Install pip
Step 3: Install boto3
  pip install boto3
Step 4: Install AWS CLI and configure AWS credentials
  aws configure
Step 5: Save the file locally
Step 6: Run the below command
python ec2_metadata.py
Step 7: To retrieve for particular data key, run below command
python ec2_metadata.py <Instance-Id>


Sample output:

 "ResponseMetadata": {
        "RequestId": "8edf551c-07f8-4ece-89ad-eecbb87b8e1a",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "8edf551c-07f8-4ece-89ad-eecbb87b8e1a",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "vary": "accept-encoding",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "4880",
            "date": "Sun, 26 Jan 2025 14:43:36 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}
