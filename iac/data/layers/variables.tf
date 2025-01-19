variable "resources" {
  description = "Resources to be search"
  type        = list(object({
    name    = string
    version = string
  }))
}