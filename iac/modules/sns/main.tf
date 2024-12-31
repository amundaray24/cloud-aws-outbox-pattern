resource "aws_sns_topic" "this" {
  name       = var.name
  fifo_topic = true
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}