resource "aws_s3_object" "this" {
  bucket  = var.bucket-name
  key     = var.key
  source  = var.path
  tags    = var.tags
}