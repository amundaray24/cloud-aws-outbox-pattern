variable "tags" {
  description = "Tags to be applied to the resources"
  type        = map(string)
  default     = {}
}

variable s3-key-layer {
  description = "S3 key for the layer"
  type        = string
  default     = "layers/layer.zip"
}

variable "buckets" {
  description = "Bucket list to create"
  default     = []
  type        = list(object({
    name      = string
  }))
}

variable "topics" {
  description = "Topic list to create"
  default     = []
  type        = list(object({
    name      = string
  }))
}

variable "subscriptions" {
  description = "Subscriptions list to create"
  default     = []
  type        = list(object({
    name                = string
    topic               = string
    retention-time      = number
    visibility-timeout  = number
    filter-policy       = map(list(string))
  }))
}

variable "dynamo" {
  description = "Resources to be created"
  default     = []
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

variable "lambdas" {
  description = "Resources to be created"
  default     = []
  type        = list(object({
    name    = string
    runtime = string
    handler = string
    timeout = number
    layers  = optional(list(object({
      name    = string
      version = string
    })),[])
    dynamo-trigger = optional(object({
      table = string
      batch-size = number
      starting-position = string
    }))
    environment-variables = map(string)
  }))
}