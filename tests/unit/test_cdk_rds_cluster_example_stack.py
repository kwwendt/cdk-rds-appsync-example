import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_rds_cluster_example.cdk_rds_cluster_example_stack import CdkRdsClusterExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_rds_cluster_example/cdk_rds_cluster_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkRdsClusterExampleStack(app, "cdk-rds-cluster-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
