variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "name" {
  description = "SNS Outbox pattern topic name"
  type        = string
}