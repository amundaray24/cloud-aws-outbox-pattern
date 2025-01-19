variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "name" {
  description = "The name of the S3 bucket"
  type        = string
}