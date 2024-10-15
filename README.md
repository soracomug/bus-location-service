# bus-location-service

# AWS Lambda Function

This is a lambda function which checks the bus location point is in the specified area or not.
This lambda function is use in the AWS IoT Core rule.

## How to develop

1. Install python 3.12 or later
2. Install dependencies
```bash
% cd aws-lambda
% pip install -r requirements.txt
% cd lambdasrc
% pip install -r requirements.txt
```
3. Develop lambda funciton in `lambdasrc` directory
4. Do test in `aws-lambda` directory
```bash
% pytest -v
```

## How to deploy

The CI/CD workflows are defined in `.github/workflows` directory.
The workflow will be triggered when push to the main branch or feature/lambda-for-iotcore-rule-engine branch.
The workflow will deploy the lambda function to the AWS Lambda when push to the main branch.

Please set the following secrets in the repository settings.

- AWS_ROLE_ARN: the ARN of the role to assume

And, set the following variables in the repository settings.

- AWS_REGION: the region of the AWS Lambda
- BUCKET_NAME: the name of the S3 bucket to store the lambda function
- LAMBDA_FUNCTION_NAME: the name of the lambda function

## How to use

Set the environment variable 'area' in the lambda function. The value of 'area' is the geojson(polygon) JSON string.
