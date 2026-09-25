resource "aws_s3_bucket_public_access_block" "devsecops_lab" {
  bucket = aws_s3_bucket.devsecops_lab.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "devsecops_lab" {
  bucket = aws_s3_bucket.devsecops_lab.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }

    bucket_key_enabled = true
  }
}

resource "aws_s3_bucket_versioning" "devsecops_lab" {
  bucket = aws_s3_bucket.devsecops_lab.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "devsecops_lab" {
  bucket = aws_s3_bucket.devsecops_lab.id

  rule {
    id     = "cleanup-old-versions"
    status = "Enabled"

    filter {}

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }

    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}
