# Welcome to your CDK TypeScript project

This is a blank project for TypeScript development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template


## AWS CLI Commands:
aws s3 ls
aws s3 cp categoryMetaData s3://cnf-product-category-metadata/ --recursive
aws s3 rm s3://YOUR_BUCKET/YOUR_FOLDER/  --recursive
`It uploads all sub directories or files to S3 recursively`