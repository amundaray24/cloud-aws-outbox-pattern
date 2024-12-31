variable "name" {
  description = "Role name"
  type        = string
}

variable "service" {
  description = "Service to attach to role"
  type        = string
}

variable "policy-arn" {
  description = "ARN of policy to attach to role"
  type        = string
}