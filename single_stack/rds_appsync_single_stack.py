from aws_cdk import Stack
from aws_cdk import aws_appsync as appsync
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_rds as rds
from constructs import Construct


class RdsClusterAppSync(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)

        api = appsync.GraphqlApi(
            self,
            "ExampleAPI",
            name="ExampleAPI",
            definition=appsync.Definition.from_file("appsync/schema.graphql"),
        )

        rds_secret = rds.Credentials.from_generated_secret(username="clusteradmin")

        vpc = ec2.Vpc(self, "AuroraVpc")

        rds_cluster = rds.ServerlessCluster(
            self,
            "AuroraCluster",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=vpc,
            credentials=rds_secret,
            cluster_identifier="db-endpoint-test2",
            default_database_name="demos",
            enable_data_api=True,
        )

        api.add_rds_data_source(
            "rds-datasource",
            rds_cluster,
            secret_store=rds_cluster.secret,
        )
