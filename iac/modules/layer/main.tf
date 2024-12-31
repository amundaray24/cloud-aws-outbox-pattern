resource "aws_lambda_layer_version" "this" {
  layer_name          = var.name
  description         = var.description
  compatible_runtimes = var.compatible-runtimes
  s3_bucket           = var.s3-bucket
  s3_key              = var.s3-key
}