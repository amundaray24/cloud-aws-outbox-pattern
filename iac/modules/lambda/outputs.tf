output "arn" {
  description = "Lambda Function ARN"
  value       = aws_lambda_function.this.arn
}

output "alias-arn" {
  description = "Lambda Alias ARN"
  value       = aws_lambda_alias.alias.arn
}