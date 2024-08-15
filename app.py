#!/usr/bin/env python3
import os

import aws_cdk as cdk
from appsync.appsync_stack import AppSyncApiStack
from rds_cluster.rds_cluster_stack import RdsClusterStack
from single_stack.rds_appsync_single_stack import RdsClusterAppSync


app = cdk.App()

env = cdk.Environment(
    account=os.getenv("CDK_ACCOUNT_DEFAULT"),
    region="us-west-2",
)

# Two stacks, One creating an RDS cluster, the other
# looks up the cluster to use as an appsync data source.
RdsClusterStack(app, "RdsClusterStack", env=env)
AppSyncApiStack(app, "AppSyncApiStack", env=env) # Cannot synth

# Creating the cluster and api in a single stack works
#RdsClusterAppSync(app, "RdsAppSyncStack", env=env)

app.synth()
