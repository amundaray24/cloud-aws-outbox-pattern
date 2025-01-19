output "buckets-arn" {
  description = "Bucket arn list"
  value       = module.buckets.arn-list
}

output "topics-arn" {
  description = "Topic arn list"
  value       = module.topics.arn-list
}

output "subscriptions-arn" {
  description = "Subscription arn list"
  value       = module.subscriptions.arn-list
}

output "dynamo-tables-arn" {
  description = "Dynamo table arn list"
  value       = module.dynamo.arn-list
}

output "dynamo-tables-stream-arn" {
  description = "Dynamo table stream arn list"
  value        = module.dynamo.streams-arn-list
}

output "lambda-arn" {
  description = "Lambda arn list"
  value       = module.lambdas.arn-list
}