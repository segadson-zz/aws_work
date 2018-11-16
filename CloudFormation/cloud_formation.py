import os
import json
import logging
import requests
import boto3

def main():
    session = boto3.Session(profile_name='pythonAutomation')
    client = session.resource('cloudformation')

    print(client)
    url = 'https://s3.amazonaws.com/cloudformation-templates-sean/vpc_cloudformation_template.yml '
    params = [
        {
            'ParameterKey': 'EnvironmentName',
            'ParameterValue': 'vpcTest',
        },
        {
            'ParameterKey': 'PrivateSubnet1CIDR',
            'ParameterValue': '10.192.20.0/24',
        },
        {
            'ParameterKey': 'PrivateSubnet2CIDR',
            'ParameterValue': '10.192.20.0/24',
        },
        {
            'ParameterKey': 'PrivateSubnet2CIDR',
            'ParameterValue': '10.192.20.0/24',
        },
        {
            'ParameterKey': 'PublicSubnet1CIDR',
            'ParameterValue': '10.192.20.0/24',
        },
        {
            'ParameterKey': 'PublicSubnet2CIDR',
            'ParameterValue': '10.192.20.0/24',
        },
        {
            'ParameterKey': 'VpcCIDR',
            'ParameterValue': '10.192.0.0/16',
        }
    ]


    response = client.create_stack(
        StackName='seanTest',
        TemplateURL='https://s3.amazonaws.com/cloudformation-templates-sean/vpc_cloudformation_template.yml',
        Parameters= params,
        #DisableRollback=True|False,
        #RoleARN='string',
        #OnFailure='DO_NOTHING'|'ROLLBACK'|'DELETE',
        #StackPolicyBody='string',
        #StackPolicyURL='string',
        #ClientRequestToken='string',
        #EnableTerminationProtection=True|False
    )

    print(response)

if __name__ == '__main__':
    main()
