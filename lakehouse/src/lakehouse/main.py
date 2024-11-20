#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack

from ckdktf_azure import AzureProvider


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AzureProvider(self, "azure", region="west-europe", features=[{}])


app = App()
MyStack(app, "lakehouse")

app.synth()
