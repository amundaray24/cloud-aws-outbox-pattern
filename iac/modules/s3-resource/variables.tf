variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "bucket-name" {
  description = "ARN of the S3 bucket"
  type        = string
}

variable "key" {
  description = "S3 key for the resource"
  type        = string
}

variable "path" {
  description = "Path to the resource"
  type        = string
}