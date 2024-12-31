output "arn" {
  description = "ARN of policy to lambda logs"
  value       = aws_iam_policy.this.arn
}