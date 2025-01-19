resource "aws_lambda_function" "this" {
  function_name = var.name
  runtime       = var.runtime
  handler       = var.handler
  role          = var.role-arn
  filename      = var.filename
  timeout       = var.time-out
  layers        = var.layers-arn
  tags          = var.tags
  environment {
    variables   = var.environment-variables
  }
  tracing_config {
    mode = "Active"
  }
}

resource "aws_lambda_alias" "alias" {
  name             = var.alias-name
  function_name    = aws_lambda_function.this.function_name
  function_version = aws_lambda_function.this.version
}