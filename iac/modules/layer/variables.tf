variable "name" {
  description = "Layer name"
  type        = string
}

variable "description" {
  description = "Lambda Layer description"
  type        = string
}

variable "s3-bucket" {
  description = "The name of the S3 bucket"
  type        = string
}

variable "s3-key" {
  description = "S3 key for the layer"
  type        = string
}

variable "compatible-runtimes" {
  description = "Compatible runtimes"
  type        = list(string)
}