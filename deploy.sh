#!/bin/bash

STACK_NAME=kms-poc
REGION=us-east-2
CLI_PROFILE=kms-poc

# Deploy the CloudFormation template
echo -e "\n\n=========== Deploying main.yml ==========="
aws cloudformation deploy --region $REGION \
    --profile $CLI_PROFILE \
    --stack-name $STACK_NAME \
    --template-file main.yml \
    --no-fail-on-empty-changeset \
    --capabilities CAPABILITY_NAMED_IAM
    

# If the deploy succeeded, show output info:
if [ $? -eq 0 ]; then
  aws cloudformation list-exports \
    --profile $CLI_PROFILE \
    --region $REGION \
    --query "Exports"
fi
