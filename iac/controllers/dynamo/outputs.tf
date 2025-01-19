output "arn-list" {
  description = "Resource arn list"
  value       = { for key, mod in module.resources : key => mod.arn }
}

output "streams-arn-list" {
  description = "Resource Streams arn list"
  value       = { for key, mod in module.resources : key => mod.stream-arn }
}