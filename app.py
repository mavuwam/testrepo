#!/usr/bin/env python3
import aws_cdk as cdk
from testrepo.testrepo_stack import TestrepoStack

app = cdk.App()
TestrepoStack(app, "TestrepoStack",
    env=cdk.Environment(account="490774640821", region="eu-west-1")
)

app.synth()
