output "arn-list" {
  description = "Resource arn list"
  value       = { for key, mod in module.resources : key => mod.arn }
}