variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "resources" {
  description = "Resources to be created"
  type        = list(object({
    name                = string
    topic               = string
    retention-time      = number
    visibility-timeout  = number
    filter-policy       = map(list(string))
  }))
}

variable "topics-arn" {
  description = "Resources dependencies arn"
  type        = map(string)
  default     = {}
}