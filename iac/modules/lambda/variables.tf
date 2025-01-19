variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "name" {
  description = "Lambda function name"
  type        = string
}

variable "runtime" {
  description = "Lambda function runtime"
  type        = string
}

variable "handler" {
  description = "Lambda function handler"
  type        = string
}

variable "role-arn" {
  description = "Lambda IAM role ARN"
  type        = string
}

# variable "s3-bucket" {
#   description = "S3 bucket name"
#   type        = string
# }
#
# variable "s3-key" {
#   description = "S3 key"
#   type        = string
# }

variable "time-out" {
  description = "Time out of the function in seconds"
  type        = number
}

variable "layers-arn" {
  description = "ARN layers list for the function"
  type        = list(string)
}

variable "environment-variables" {
  description = "Environment variables for lambda function"
  type        = map(string)
}

variable "alias-name" {
  description = "Name of the lambda function alias"
  type        = string
}

variable "filename" {
  description = "Path to the function's deployment package"
  type        = string
}
