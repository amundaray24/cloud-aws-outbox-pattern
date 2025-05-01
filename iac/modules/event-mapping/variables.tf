variable "source-arn" {
  description = "Event source ARN"
  type        = string
}

variable "lambda-arn" {
  description = "Lambda target ARN"
  type        = string
}

variable "lambda-alias-name" {
  description = "Lambda target alias name"
  type        = string
}

variable "starting-position" {
  description = "starting position of the event source mapping"
  type        = string
  default     = null
}

variable "batch-size" {
  description = "Batch size"
  type        = number
}

variable "maximum-retry-attempts" {
  description = "Maximum retry attempts"
  type        = number
  default     = null
}