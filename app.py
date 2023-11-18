#!/usr/bin/env python3
import aws_cdk as cdk
from testrepo.testrepo_stack import testrepo_stack

app = cdk.App()
testrepo_stack(app, "testrepo_stack",
    env=cdk.Environment(account="490774640821", region="eu-west-1")
)

app.synth()
