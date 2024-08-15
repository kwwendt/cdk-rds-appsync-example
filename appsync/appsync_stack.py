from aws_cdk import Stack, aws_appsync as appsync, aws_rds as rds, aws_secretsmanager
from constructs import Construct


class AppSyncApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)

        api = appsync.GraphqlApi(
            self,
            "ExampleAPI",
            name="ExampleAPI",
            definition=appsync.Definition.from_file('appsync/schema.graphql'),
        )

        rds_secret = aws_secretsmanager.Secret.from_secret_partial_arn(
            self,
            "rds-secret",
            secret_partial_arn=f"arn:aws:secretsmanager:{stack.region}:{stack.account}:secret:RdsClusterStackAuroraCluste-nRwpQKS9XavU",
        )


        rds_cluster = rds.DatabaseCluster.from_database_cluster_attributes(
            self,
            "ClusterFromOtherStack",
            cluster_identifier="db-endpoint-test",
        )


        api.add_rds_data_source(
            'rds-datasource',
            rds_cluster,
            secret_store=rds_secret,
        )
