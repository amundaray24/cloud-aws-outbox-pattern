variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "name" {
  description = "Policy name"
  type        = string
}

variable "description" {
  description = "Description of the policy"
  type        = string
}

variable "policy" {
  description = "ARN of the secret to access"
  type        = any
}