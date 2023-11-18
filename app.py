#!/usr/bin/env python3
import aws_cdk as cdk
from testrepo.testrepo_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="490774640821", region="eu-west-1")
)

app.synth()
