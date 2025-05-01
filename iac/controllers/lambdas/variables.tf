variable "resources" {
  description = "Resources to be created"
  default     = []
  type        = list(object({
    name    = string
    runtime = string
    handler = string
    timeout = number
    layers  = optional(list(object({
      name    = string
      version = string
    })),[])
    dynamo-trigger = optional(object({
      table = string
      batch-size = number
      starting-position = string
      maximum-retry-attempts = number
    }))
    sqs-trigger = optional(object({
      queue = string
      batch-size = number
    }))
    environment-variables = map(string)
  }))
}

variable "role-arn" {
  description = "ARN of the IAM role to be used by the Lambda function"
  type        = string
}

variable "filename" {
  description = "Default code to be used by the Lambda function"
  type        = string
}

variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}