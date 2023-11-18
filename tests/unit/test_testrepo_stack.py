import aws_cdk as core
import aws_cdk.assertions as assertions

from testrepo.testrepo_stack import TestrepoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in testrepo/testrepo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestrepoStack(app, "testrepo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
