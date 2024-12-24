from cdktf import App

from stratum.stacks.terraform_backend import TerraformBackendStack

if __name__ == "__main__":
    app = App()
    TerraformBackendStack(app, "terraform-backend")
    app.synth()
