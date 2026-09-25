resource "aws_s3_bucket" "devsecops_lab" {
  bucket = "devsecops-lab-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "DevSecOps Lab"
    Environment = "Lab"
    ManagedBy   = "Terraform"
  }
}

data "aws_caller_identity" "current" {}
