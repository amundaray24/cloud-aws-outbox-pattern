resource "aws_lambda_function" "this" {
  function_name = var.name
  runtime       = var.runtime
  handler       = var.handler
  role          = var.role-arn
  s3_bucket     = var.s3-bucket
  s3_key        = var.s3-key
  timeout       = var.time-out
  layers        = var.layers-arn
  environment {
    variables   = var.environment-variables
  }
  tracing_config {
    mode = "Active"
  }
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}

resource "aws_lambda_alias" "alias" {
  name             = var.alias-name
  function_name    = aws_lambda_function.this.function_name
  function_version = aws_lambda_function.this.version
}