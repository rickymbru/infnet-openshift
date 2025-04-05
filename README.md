# infnet-openshift
Projeto Final - Administração de Containers com Red Hat OpenShift [25E1_3]

# Install Terraform
Follow the official Hashcorp instructions [here](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli), choose one of available instructions corresponding to your operacional system.

# Complete the credentials file
Get your aws credentials and insert intro `creds.txt` file on root repo directory:

```sh
[default]
aws_access_key_id=******************
aws_secret_access_key=******************
aws_session_token=******************
```

# Terraform
On your command line interface at the terraform-file directory, follow the steps:

- E.g. `infnet-openshift/rancher-k3s-rke2`:

### Initialize Terraform
```sh
terraform init
```
### Plan and Apply
```sh
terraform plan
terraform apply
```
### Removing created resources
```sh
terraform destroy
```
