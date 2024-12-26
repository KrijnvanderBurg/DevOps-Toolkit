"""
Tests of main module for the Stratum application.
"""

# import pytest
from cdktf import TerraformStack, Testing

# The tests below are example tests, you can find more information at
# https://cdk.tf/testing


class TestMain:
    """
    TestMain is a test class for validating the Terraform stack configuration.

    Attributes:
        stack (TerraformStack): An instance of TerraformStack used for testing.

    Methods:
        test_should_contain_container: Checks if the synthesized stack contains a container resource.
        test_should_use_an_ubuntu_image: Verifies that the container resource uses the Ubuntu latest image.
        test_check_validity: Validates the synthesized Terraform configuration.
    """

    stack = TerraformStack(Testing.app(), "stack")
    # app_abstraction = MyApplicationsAbstraction(stack, "app-abstraction")
    # synthesized = Testing.synth(stack)

    # def test_should_contain_container(self):
    #    assert Testing.to_have_resource(self.synthesized, Container.TF_RESOURCE_TYPE)

    # def test_should_use_an_ubuntu_image(self):
    #    assert Testing.to_have_resource_with_properties(self.synthesized, Image.TF_RESOURCE_TYPE, {
    #        "name": "ubuntu:latest",
    #    })

    # def test_check_validity(self):
    #    assert Testing.to_be_valid_terraform(Testing.full_synth(stack))
