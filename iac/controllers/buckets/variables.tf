variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "resources" {
  description = "Resources to be created"
  type        = list(object({
    name        = string
  }))
}