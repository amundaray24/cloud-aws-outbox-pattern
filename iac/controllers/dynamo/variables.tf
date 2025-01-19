variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
}

variable "resources" {
  description = "Resources to be created"
  type        = list(object({
    name                      = string
    hash-key-name             = string
    range-key-name            = string
    billing-mode              = string
    stream-enabled            = bool
    stream-view-type          = string
    attributes                = list(object({
      name = string
      type = string
    }))
    global-secondary-indexes  = list(object({
      name            = string
      hash-key        = string
      projection-type = string
    }))
  }))
}