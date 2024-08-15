 # AWS CDK Issue Example

 Example repo to reproduce issue: https://github.com/aws/aws-cdk/issues/31116

 Steps to repro:

 Create and activate virtual env:
 `python -m venv .venv`
 `source .venv/bin/activate`

 Install requirements:
 `pip install -r requirements.txt`
 `npm install -g aws-cdk`


With a combined stack creating an RDS cluster and AppSync API, synth and deploy works fine:
`CDK_ACCOUNT=<account_id> cdk synth`
or
`CDK_ACCOUNT=<account_id> cdk deploy`

but if you comment out the [RdsClusterStack](https://github.com/TonySherman/cdk-rds-appsync-example/blob/main/app.py#L24)
and uncomment the [two separate stacks](https://github.com/TonySherman/cdk-rds-appsync-example/blob/main/app.py#L20-L21),
the error is thrown:

`RuntimeError: Error: Cannot grant Data API access when the Data API is disabled`
