##Source
##https://github.com/deepeshuniyal/aws_sts_get-session-token.git

import configparser
import os.path
import sys
import os
import boto3
#import click

''' Allowed values between 900 - 43200 sec (12 hrs). '''
TOKEN_DURATION = 43200
REGION = 'ap-south-1'
mfa_device_arn='arn:aws:iam::4272323553435:mfa/deepesk'
mfa_code = raw_input("Enter the mfa code : ")
def get_tokens(mfa_device_arn=None, mfa_code=None):
    """ Get new session tokens with AWS Security Token Service.
        The default profile is used to get new tokens.
    """
    session = boto3.Session(profile_name='default')
    client = session.client('sts')
    print("wating for resonse from AWS....")
    response = client.get_session_token(
        DurationSeconds=TOKEN_DURATION,
        SerialNumber=mfa_device_arn,
        TokenCode=mfa_code
    )
    print("Response : [{0}]".format(response))
    tokens = {
        'output': 'json',
        'region': REGION,
        'aws_access_key_id': response['Credentials']['AccessKeyId'],
        'aws_secret_access_key': response['Credentials']['SecretAccessKey'],
        'aws_session_token': response['Credentials']['SessionToken']
    }

    ##print("Token expiration: {response['Credentials']['Expiration']}")

    return tokens

data = get_tokens(mfa_device_arn,mfa_code)

f = open("{0}/.aws/.aws_access_data".format(os.environ['HOME']), "w+")
f.write("export AWS_ACCESS_KEY_ID={0}\n".format(data['aws_access_key_id']))
#f.close()

#f = open("~/.aws/.aws_access_data", "a")
f.write("export AWS_SECRET_ACCESS_KEY={0}\n".format(data['aws_secret_access_key']))
f.write("export  AWS_SESSION_TOKEN={0}\n".format(data['aws_session_token']))
f.close()
#. ~/.bashrc
