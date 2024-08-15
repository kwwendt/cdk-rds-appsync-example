#!/usr/bin/env python3
import os

import aws_cdk as cdk
from appsync.appsync_stack import AppSyncApiStack
from rds_cluster.rds_cluster_stack import RdsClusterStack


app = cdk.App()

env = cdk.Environment(
    account=os.getenv("CDK_ACCOUNT"),
    region="us-east-1",
)


RdsClusterStack(app, "RdsClusterStack", env=env)

AppSyncApiStack(app, "AppSyncApiStack", env=env)

app.synth()
