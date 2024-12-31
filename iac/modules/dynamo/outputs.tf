output "arn" {
  description = "ARN of dynamo table"
  value       = aws_dynamodb_table.this.arn
}

output "stream-arn" {
  description = "ARN of stream of dynamo table"
  value       = aws_dynamodb_table.this.stream_arn
}