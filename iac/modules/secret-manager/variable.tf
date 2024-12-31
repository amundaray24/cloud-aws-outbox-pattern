variable "name" {
  description = "Secret manager name of the secret"
  type        = string
}

variable "description" {
  description = "Secret manager description of the secret"
  type        = string
}

variable "recovery-window-in-days" {
  description = "Secret manager recovery window in days"
  type        = number
}