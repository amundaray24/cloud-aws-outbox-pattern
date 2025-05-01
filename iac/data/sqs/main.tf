data "aws_sqs_queue" "sqs-queue" {
  name  = var.name
}