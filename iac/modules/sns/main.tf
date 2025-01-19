resource "aws_sns_topic" "this" {
  name        = var.name
  fifo_topic  = true
  tags        = var.tags
}