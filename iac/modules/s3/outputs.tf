output "name" {
  description = "The name of the S3 bucket"
  value       = var.name
}
output "arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.this.arn
}