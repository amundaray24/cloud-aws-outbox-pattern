variable "name" {
  description = "DynamoDB table name"
  type        = string
}

variable "hash-key-name" {
  description = "DynamoDB table hash key name"
  type        = string
}

variable "hash-key-type" {
  description = "DynamoDB table hash key type"
  type        = string
  default     = "S"
}

variable "range-key-name" {
  description = "DynamoDB table range key name"
  type        = string
}

variable "range-key-type" {
  description = "DynamoDB table range key type"
  type        = string
  default     = "S"
}

variable "billing-mode" {
  description = "DynamoDB table billing mode"
  type        = string
  default     = "PAY-PER-REQUEST"
}