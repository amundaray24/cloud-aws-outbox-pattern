variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "name" {
  description = "DynamoDB table name"
  type        = string
}

variable "hash-key-name" {
  description = "DynamoDB table hash key name"
  type        = string
}

variable "range-key-name" {
  description = "DynamoDB table range key name"
  type        = string
}

variable "attributes" {
  description = "DynamoDB table attributes"
  type        = list(object({
    name = string
    type = string
  }))
}

variable "billing-mode" {
  description = "DynamoDB table billing mode"
  type        = string
  default     = "PAY-PER-REQUEST"
}

variable "stream-enabled" {
  description = "DynamoDB stream is enable"
  type        = bool
  default     = false
}

variable "stream-view-type" {
  description = "DynamoDB stream view type"
  type        = string
  default     = "NEW_AND_OLD_IMAGES"
}

variable "global-secondary-indexes" {
  description = "DynamoDB table global secondary index"
  type        = list(object({
    name            = string
    hash-key        = string
    projection-type = string
  }))
  default     = []

  validation {
    condition     = length(var.global-secondary-indexes) <= 20
    error_message = "Global secondary indexes must be less than or equal to 20"
  }
}