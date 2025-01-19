variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "topic-arn" {
  description = "SNS Outbox pattern topic ARN"
  type        = string
}

variable "name" {
  description = "SQS queue name"
  type        = string
}

variable "retention-time" {
  description = "SQS retention seconds"
  type        = number
  default     = 604800
}

variable "filter-policy" {
  description = "SQS filter policy"
  type        = any
}

variable "visibility-timeout" {
  description = "SQS visibility timeout"
  type        = number
}

variable "visibility-timeout-dlq" {
  description = "SQS DLQ visibility timeout"
  type        = number
  default     = 30
}