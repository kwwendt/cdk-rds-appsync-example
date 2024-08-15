from aws_cdk import (
    Stack,
    aws_rds as rds,
    aws_ec2 as ec2,
)
from constructs import Construct


class RdsClusterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "AuroraVpc")

        cluster = rds.ServerlessCluster(
            self,
            "AuroraCluster",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=vpc,
            credentials=rds.Credentials.from_generated_secret(username="clusteradmin"),
            cluster_identifier="db-endpoint-test",
            default_database_name="demos",
            enable_data_api=True,
        )
